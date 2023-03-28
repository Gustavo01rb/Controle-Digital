//DTFT DE UMA UNICA SEQUENCIA
clc ;
clear ;
// a =0 . 5 ;
n=0:9;
x=[1,zeros(1,9) ];
disp(x, 'x[n] =' )

K = 4;
k = 0:4/100:4;
W = k*2* %pi/K;
X=(x)*exp(%i*n'*W);
disp (X, 'DTFT, x[n]' )
X_mag= abs(X);
X_phase= phasemag(X); // não existe fase, apenas 1 espectro
figure(0);
plot2d3( mtlb_fliplr(W),X_mag );

xtitle( 'Modulo' , 'Omega' , 'Magnitude' );
figure(1);
plot2d3(mtlb_fliplr(W),X_phase);

xtitle('zero fase' , 'Omega' , 'Angulo' );
