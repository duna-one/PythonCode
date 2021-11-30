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

def system( in_signal, prev_in_signal, prev_out_signal, fb_signal ):
    '''Функция системы'''	
    out_signal = in_signal + gain( prev_out_signal, -1.0 ) #сумматор 1
    out_signal = gain( out_signal, 11.9)
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

#текстовый вывод
outxt = open( 'out.txt', 'w+' )
outxt.write(' i      x[i]       y[i] ')
ins = [0]*N
outs = [0]*N
fbs = [0]*N
t = list( range(N) )
for i in t:
    if i == 0:
        ins[0], outs[0], fbs[0] = system( 0, 0, 0, 0)
    elif i == 1 or i == 2:
        ins[i], outs[i], fbs[i] = system(0, ins[i-1], outs[i-1], fbs[i-1])
    else:
        ins[i], outs[i], fbs[i] = system(1, ins[i-1], outs[i-1],  fbs[i-1])

    outxt.write('\n'+ '{:<5} {:<10} {:<10}'.format (i+1, str(ins[i]) [:9], str(outs[i]) [:9] ) )
    t[i] = round( 0.8*i, 2)
outxt.close()   

#графический вывод
import pylab
pylab.title( 'График' )
pylab.xlabel( 't, сек ' )
pylab.ylabel( 'Y[t] ' )
pylab.grid( axis='both' )
pylab.plot( t, outs )
pylab.show ()





 
