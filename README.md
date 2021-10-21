Deploy to Streamlit
- Create `.env` file and populate like this

```
clientId = "xxxxxxxxxxxx"
domain = "dev-xxxx.us.auth0.com"
```

- `streamlit run test.py` to test locally
- on local instance on streamlit interface right click on 3-dot top right and click deploy this app
- when authorizing app under "Advanced Settings" (screenshot 1.png) set the below

```
clientId = "xxxxxxxxxxxx"
domain = "dev-xxxx.us.auth0.com"
``

