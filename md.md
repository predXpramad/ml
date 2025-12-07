```latex
\begin{figure}[h]
\centering
\begin{tikzpicture}[
    node distance=12mm,
    block/.style={rectangle, draw, rounded corners, align=center, minimum width=6.5cm, minimum height=1.2cm},
    decision/.style={diamond, draw, aspect=2, align=center},
    startstop/.style={ellipse, draw, align=center, minimum width=3cm},
    line/.style={draw, -latex'}
]

\node[startstop] (start) {Start};

\node[block, below=of start] (acq) {Video Acquisition\\(Camera Input)};

\node[block, below=of acq] (prep) {Preprocessing\\Brightness \& Resolution Normalization};

\node[block, below=of prep] (yolo) {YOLO-based Facial-State Detection\\(Real-Time)};

\node[block, below=of yolo] (temp) {Temporal Behaviour Analysis\\
Track Eye Closure, Yawning, Engagement};

\node[decision, below=of temp] (eval) {Fatigue Indicator\\Exceeded?};

\node[block, right=20mm of eval] (alert) {Alert Module\\
Visual \& Audio Alerts\\Flash Overlay\\WhatsApp Escalation};

\node[block, below=of eval] (log) {Logging Module\\State Samples \& Events};

\node[block, below=of log] (report) {Summary Report Generation\\(End of Session)};

\node[startstop, below=of report] (stop) {Stop};

\node[block, left=20mm of eval] (emergency) {Emergency-Assistance Button};

% Connections
\path[line] (start) -- (acq);
\path[line] (acq) -- (prep);
\path[line] (prep) -- (yolo);
\path[line] (yolo) -- (temp);
\path[line] (temp) -- (eval);

\path[line] (eval.east) -- (alert);
\path[line] (eval.south) -- (log);
\path[line] (log) -- (report);
\path[line] (report) -- (stop);

\path[line] (emergency) -- (log);
\path[line] (alert) |- (log);

\end{tikzpicture}
\caption{Workflow of the System (Figure X)}
\label{fig:workflow}
\end{figure}
```
