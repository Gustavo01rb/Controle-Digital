//MODULO E ANGULO
clc ;
clear ;

a =0.5;
n =0:9;
    for i = 0:9
      x(i+1) = (a* exp (-%i* %pi ))^i; //x[n]]
    end

fator=100;

K = 4;
k = 0:4/fator:4; //dominio temporal t
W = k*6* %pi /K;
X = (x')* exp (%i*n'*W); //X(ejomega)

X_mag = abs(X);
X_phase = phasemag (X);

a= gca ();
figure (0);
plot2d3 ( mtlb_fliplr (W),X_mag );
xtitle ( 'Ganho( modulo)' , 'Omega w' , ' Amplitude ' );
figure (1);
plot2d3 ( mtlb_fliplr (W),X_phase );
xtitle ( 'Fase( angulo)' , 'Omega w' , 'angulo ( Teta)' );

figure (2);
plot2d3(n,x);
xtitle ( 'Amplitude sinal' , 'n (tempo discreto)' , 'angulo ( Teta)' );






