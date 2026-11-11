# Running this project

This import is a static HTML redirect page, not a full application.

- Click **Run** to start the **Start application** workflow.
- The workflow runs `python3 server.py` on `0.0.0.0:5000`.
- No third-party dependencies, secrets, or external services are required.
- The server serves only `/` and `/index.html`; other project files are not public.

## Existing behavior

`index.html` immediately navigates to `https://www.google.com`, preserving
the URL fragment (the text after `#`). This behavior is unchanged.
Google may refuse to display inside Replit's embedded preview. Open the
preview in a separate browser tab to use the redirect.
