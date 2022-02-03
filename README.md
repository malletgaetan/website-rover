# website-rover
Lightweight python script that try to discover every route of a website without any browser driver

## How to use
Currently script is a its simplest, some enhancement are to come

replace https://www.python.org with the url of your choice
```bash
python3 main.py https://www.python.org
```

Once the script as finished, you can see results by using:
```bash
cat <url_requested>.txt
```

## Enhancements

- [ ] support custom HTTP headers (authentication website)
- [ ] handle rate limiting
- [ ] handle list of proxies
- [ ] options to handle when a url should be taged as "valid" and added to list (responding to GET request, being referenced)
