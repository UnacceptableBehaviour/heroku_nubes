= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Ex3 - Point domain name to APP (& setup SSL next..)

### Domain name: theunfinishedproject.space
### DNS Target: molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com
### Application URL: https://stark-scrubland-88399.herokuapp.com/
### Application name: stark-scrubland-88399
#### 
#### photography kindly provided by ferdiesfoodlab.co.uk
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

## Steps:

## Add custom domain
```
$ heroku domains:add www.theunfinishedproject.space
Adding www.theunfinishedproject.space to ⬢ stark-scrubland-88399... done
▸    Configure your app's DNS provider to point to the DNS Target computational-partridge-c23ms6gex8rmypn3hre1osid.herokudns.com.
▸    For help, see https://devcenter.heroku.com/articles/custom-domains

The domain www.theunfinishedproject.space has been enqueued for addition
▸    Run heroku domains:wait 'www.theunfinishedproject.space' to wait for completion
```

## have a look at current domain settings:
```
$ heroku domains

=== stark-scrubland-88399 Heroku Domain
stark-scrubland-88399.herokuapp.com

=== stark-scrubland-88399 Custom Domains
Domain Name                     DNS Record Type  DNS Target
──────────────────────────────  ───────────────  ──────────────────────────────────────────────────────────────
www.theunfinishedproject.space  CNAME            computational-partridge-c23ms6gex8rmypn3hre1osid.herokudns.com
```

DNS provider: namecheap.com

## Checking propagation for DNS complete
```
$ host www.theunfinishedproject.space
www.theunfinishedproject.space is an alias for parkingpage.namecheap.com.
parkingpage.namecheap.com has address 198.54.117.218
parkingpage.namecheap.com has address 198.54.117.211
parkingpage.namecheap.com has address 198.54.117.210
parkingpage.namecheap.com has address 198.54.117.215
parkingpage.namecheap.com has address 198.54.117.217
parkingpage.namecheap.com has address 198.54.117.216
parkingpage.namecheap.com has address 198.54.117.212
```

## Not sure waht effect this actually has
$ heroku domains:wait 'www.theunfinishedproject.space'


## Add root domain
```
$ heroku domains:add theunfinishedproject.space
Adding theunfinishedproject.space to ⬢ stark-scrubland-88399... done
▸    Configure your app's DNS provider to point to the DNS Target molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com.
▸    For help, see https://devcenter.heroku.com/articles/custom-domains

The domain theunfinishedproject.space has been enqueued for addition
▸    Run heroku domains:wait 'theunfinishedproject.space' to wait for completion
$
```


## Pointing a domain to a heroku app:
(This is for namecheap.com DNS - see link in Refs)
Login . .
Mangage Domain > Advanced > set as below
```
CNAME                    www                            molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com
URL Redirect Record        @                            http://www.theunfinishedproject.space
URL Redirect Record        theunfinishedproject.space        http://theunfinishedproject.space
```

Check after propagation (TTL set to 5min):
```
(venv-heroku) Simons-MacBook-Pro-2:heroku_nubes simon$ heroku domains
=== stark-scrubland-88399 Heroku Domain
stark-scrubland-88399.herokuapp.com

=== stark-scrubland-88399 Custom Domains
Domain Name                     DNS Record Type  DNS Target
──────────────────────────────  ───────────────  ──────────────────────────────────────────────────────────────
www.theunfinishedproject.space  CNAME            computational-partridge-c23ms6gex8rmypn3hre1osid.herokudns.com
theunfinishedproject.space      ALIAS or ANAME   molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com


$ host www.theunfinishedproject.space
www.theunfinishedproject.space is an alias for molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com.
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 35.173.3.255
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 52.22.145.207
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 52.2.175.150
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 34.231.75.48
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 52.73.9.93
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 54.173.32.212
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 52.72.230.122
molecular-pumpkin-rulu5keb86w502k76rzcj2lb.herokudns.com has address 52.54.84.112
(venv-heroku) Simons-MacBook-Pro-2:heroku_nubes simon$ host theunfinishedproject.space
theunfinishedproject.space has address 162.255.119.235
theunfinishedproject.space mail is handled by 10 eforward2.registrar-servers.com.
theunfinishedproject.space mail is handled by 20 eforward5.registrar-servers.com.
theunfinishedproject.space mail is handled by 10 eforward3.registrar-servers.com.
theunfinishedproject.space mail is handled by 15 eforward4.registrar-servers.com.
theunfinishedproject.space mail is handled by 10 eforward1.registrar-servers.com.
```

We have a live website - yeay!
Image quality terrible - shrank them a bit too much!


## Next:
#### What’s SSL endpoint addon?
#### Can we even do SSL from this DNS provder?
#### How to create an SSL certificate hope fully with letsencrypt

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
## REFERENCES
### Custom Domain Names - theunfinishedproject.space
https://devcenter.heroku.com/articles/custom-domains

### fcc - intro to DNS
https://www.freecodecamp.org/news/understanding-the-domain-name-servers-46c6bcf9afa3/

### Pointing a domain to a heroku app: This is for namecheap.com DNS
https://www.namecheap.com/support/knowledgebase/article.aspx/9737/2208/pointing-a-domain-to-the-heroku-app

### SSL
https://letsencrypt.org/getting-started/

### SSL - namecheap
https://www.namecheap.com/support/live-chat/ssl/
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

