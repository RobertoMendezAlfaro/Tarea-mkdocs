# Descripción del método
## Método Runge-Kutta de orden 4 (RK4)

Este método funciona mediante el uso de las siguientes equaciones:

\begin{aligned}
k_1 &= hf(t_n,y_n)\\
k_2 &= hf(t_n + \frac{h}{2}, y_n + \frac {k_1}{2}) \\
k_3 &= hf(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}) \\
k_4 &= hf(t_n + h, y_n + K_3) \\
\end{aligned}

Con estas ecuaciones se puede construir la ecuación que describe la evolucion del sistema conforme pasa el tiempo:

\begin{aligned}
y_{n+1} &\rightarrow y_n + \frac{1}{6}(k_1 +2k_2 +2k_3 +k_4)\\
\end{aligned}

Esta ecuación nos permite aproximar el estado actual del sistema dado el estado previo de este.
