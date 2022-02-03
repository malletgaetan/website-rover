# website-rover
Lightweight python script that try to discover every route of a website without any browser driver

## how to use
Currently script is a its simplest, some enhancement are to come.

To start search for website routes:
```bash
python3 main.py https://<url>
```

Once the script as finished, you can see results by using:
```bash
cat <url>.txt
```

## rate limiting
Currently website-rover isn't handling rate limiting.

But you can test if a website is actually rate limiting by running:
```bash
python3 rate_limit_tester.py https://<url>
```

## enhancements

- [ ] support custom HTTP headers (authentication website)
- [ ] handle rate limiting
- [ ] handle list of proxies
- [ ] options to handle when a url should be taged as "valid" and added to list (responding to GET request, being referenced)
