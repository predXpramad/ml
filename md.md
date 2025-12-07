```mermaid
flowchart TD

    A([Start]) --> B[Video Acquisition (Camera Input)]
    B --> C[Preprocessing<br/>Brightness & Resolution Normalization]
    C --> D[YOLO-based Facial-State Detection<br/>(Real-Time)]
    D --> E[Temporal Behaviour Analysis<br/>- Eye Closure<br/>- Yawning<br/>- Engagement Decline]

    E --> F{Fatigue Indicator<br/>Exceeded?}

    F -->|Yes| G[Alert Module<br/>Visual & Audio Alerts<br/>Flash Overlay<br/>WhatsApp Escalation]
    F -->|No| H[Logging Module<br/>State Samples & Events]

    G --> H
    H --> I[Summary Report Generation<br/>(End of Session)]
    I --> J([Stop])

    K[Emergency-Assistance Button] --> H

```
