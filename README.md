# website-rover
Lightweight script that try to discover every route of a website, backend or frontend generated, without any browser driver

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

In the case the script tells you that he's actually getting rate limited, then this tools can't help you at this time ¯\_(ツ)_/¯

## enhancements

- [x] support custom HTTP headers (authentication website)
- [x] add browser headers
- [ ] handle list of proxies
