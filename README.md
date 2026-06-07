# About This Project
I wanted to learn how LLM works so I asked AI to recommend a project that I can do over the weekend. It suggested a tool for probing and logging LLM API responses for behavioral anomalies. I then asked it to generate a project blueprint that I can follow. We're calling it `llm_probe`, a tool that sends categorized prompts to an LLM, logs the responses, and highlights potentially interesting behavior for further analysis.



# Project Structure / Architecture
```
llm-probe/
├── probe.py          # main runner
├── prompts.py        # your test prompt library
├── logger.py         # response logging
├── analyzer.py       # anomaly detection logic
├── results/          # output logs (gitignored if sensitive)
└── README.md         # documents methodology and findings
```

`probe.py` — a simple loop that:

- Takes a prompt from a list
- Sends it to the API
- Receives the response
- Logs the full exchange with timestamp, prompt, response, token count, and latency

    ```plaintext
    Prompt
    │
    ▼
    LLM API
    │
    ▼
    Response
    │
    ├────────► Logger
    │              │
    │              ▼
    │          JSON / CSV
    │
    └────────► Analyzer
                    │
                    ▼
                Anomaly Flags
    ```

`prompts.py` — Contains data only, classified into 7 categories, ~45 prompts total. All labeled and commented to define what each category is testing and why.
 
 `logger.py` — Simply recordes evidence. It saves each exchange to a structured JSON or CSV file.

`analyzer.py` — flags anomalies automatically: refusals, length outliers, hedging, instruction violations, and potential prompt injection compliance.





