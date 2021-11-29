#ввод данных
flag = True
while flag:
    try:
        N = input ( 'Введите число интервалов входного сигнала:   ' )
        N = int(N)
        if N <= 0:
            print ( 'Введено неправильное число!' )
        else:
            print ( 'Введено: ', N )
            flag = False;
    except Exception:
        print ( 'Введено неправильное число!' )

flag = True
while flag:
    try:
        coef_min = input( 'Введите наименьшее значение варьируемых коэффициентов:   ')
        coef_min = float(coef_min)
        print ( 'Минимальное значение коэффициентов: ', coef_min )
        flag = False;
    except Exception:
        print ( 'Введено неправильное число!' )

flag = True
while flag:
    try:
        coef_max = input( 'Введите наибольшее значение варьируемых коэффициентов:   ')
        coef_max = float(coef_max)
        if coef_max <= coef_min:
                print ('Ошибка - максимаьное значение больше минимального!')
        else:
            print ( 'Максимальное значение коэффициентов: ', coef_max )
            flag = False;
    except Exception:
        print ( 'Введено неправильное число!' )

flag = True
while flag:
    try:
        step = input( 'Введите положительный шаг варьирования:  ')
        step = float(step)
        if step <= 0:
            print ( 'Введено неправильное число!' )
        else:
            print ( 'Шаг варьирования: ', step )
            flag = False;
    except Exception:
        print ( 'Введено неправильное число!' )

def gain( in_signal, K ):
    '''Усилитель'''	
    return K*in_signal

def elast_link( in_signal, prev_in_signal, prev_out_signal, T1, T2 ):
    '''Упругое звено'''	
    return (T1*prev_out_signal+in_signal* (1+T2)-T2*prev_in_signal) /(1+T1)

def inert_link( in_signal, prev_out_signal, T ):
    '''Инерционное звено'''	
    return ( in_signal + T*prev_out_signal )/( 1 +T)

def integrator( in_signal, prev_out_signal ):
    '''Интегратор'''	
    return 0.001*in_signal + prev_out_signal

def diff_link( in_signal, prev_in_signal, prev_out_signal, T ):
    '''Дифференцирующее звено'''	
    return ( T*prev_out_signal + in_signal - prev_in_signal )/( 1+T)

def system( K1, K3, in_signal, prev_in_signal, prev_out_signal, fb_signal):
    '''Функция системы'''
    out_signal = in_signal + gain( prev_out_signal, K3 ) #сумматор 1
    out_signal = gain( out_signal, K1 )
    out_signal= elast_link (out_signal, prev_in_signal, prev_out_signal, 0.134, 0.0303)
    out_signal = out_signal + fb_signal #сумматор 2
    out_signal = inert_link( out_signal, prev_out_signal, 0.0616 )
#вторая ветвь обратной связи
    fb_signal = out_signal
    fb_signal = diff_link( fb_signal, prev_in_signal, prev_out_signal, 0.134 )
    fb_signal = gain( fb_signal, -0.1 )
    out_signal = inert_link( out_signal, prev_out_signal, 0.15 )
    out_signal = integrator( out_signal, prev_out_signal )
    return in_signal, out_signal, fb_signal

#вывод графиков 
import pathlib, numpy, pylab
filepath = str( pathlib.Path().absolute() )
coef_range = list( numpy.arange( coef_max, coef_min-1, -step ) )
plots_yx = round(( coef_max-coef_min )/ step ) + 1
plot, axes = pylab.subplots(nrows=plots_yx, ncols=plots_yx, figsize=(plots_yx, plots_yx) )
plot.suptitle('Варьирование коэффициентов' )
j = plots_yx-1
for K1 in coef_range:
    K1 = round( K1, 2 )
    k=0
    for K3 in coef_range:
        K3 = round( K3, 2 )
        ins = [0]*N
        outs = [0]*N
        fbs = [0]*N
        t = list( range(N) )
        for i in t:
            if i==0 :
                ins[0], outs[0], fbs[0] = system( K1, K3, 0, 0, 0, 0)
            elif i == 1 or i == 2:
                ins [i], outs[i], fbs[i] = system(K1,K3,0,ins[i-1],outs[i-1], fbs[i-1])
            else:
                ins [i], outs[i], fbs[i] = system(K1,K3,1,ins[i-1],outs[i-1], fbs[i-1])
            t[i] = round( 0.8*i, 2)
        axes[ k, j ].plot( t, outs )
        axes[ k, j ].set_title( 'K1= ' + str(K1) + ' K3=' + str(K3) )
        print ( 'Построен график для К1=  ' + str(K1) + ', K3=' + str(K3) )
        k +=1
    if K1 == coef_range[ len(coef_range)-1 ]:
        print( 'Построение завершено' )
    j -=1
plot.savefig( filepath + '\\variation.png' )
