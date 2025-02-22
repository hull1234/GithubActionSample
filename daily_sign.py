import os
import requests

cookie = os.environ.get("JD_COOKIE")

url = ("https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1"
       "%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1"
       "%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14"
       ".8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp"
       "=jsonp_1645885800574_58482")

headers = {"Connection": 'keep-alive',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cache-Control": 'no-cache',
           "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
           "accept": "*/*",
           "connection": "Keep-Alive",
           "Accept-Encoding": "gzip,deflate",
           "Cookie": "__jdu=1090644581; shshshfpa=f507d5db-9187-f3cd-b8db-63db1ab40c12-1694929666; TrackID=1As-3_XcfcwOV-tZF3SzSfm9UmmLOIg-qL7ZkW-nON8zhJcL-gQhWDV70XC2_K8GC1XcH3QIYIilVdds2YGV0xmuKydRSJLTHLp8-D4bDrQw46vDXsR0JEIXWnTvwBVbZ; 3AB9D23F7A4B3C9B=GVTB6UHAPJLV2ZFD55FZO2A24P3VUF7EFNYXPRZSNWF37LC542XP6T4CXSVJIN7Y6KZE4GCTWQTHXELQJDJF4QVHWI; __jda=76161171.1090644581.1694929665.1728745653.1740187317.15; __jdc=76161171; __jdv=76161171|baidu|-|organic|notset|1740187316862; 3AB9D23F7A4B3CSS=jdd03GVTB6UHAPJLV2ZFD55FZO2A24P3VUF7EFNYXPRZSNWF37LC542XP6T4CXSVJIN7Y6KZE4GCTWQTHXELQJDJF4QVHWIAAAAMVFM7TJSIAAAAAC22WJKWAIWGI6MX; _gia_d=1; areaId=15; ipLoc-djd=15-1213-0-0; PCSYCityID=CN_330000_330100_0; shshshfpx=f507d5db-9187-f3cd-b8db-63db1ab40c12-1694929666; shshshfpb=BApXSu683KPBA8XvLY8AdeQoSCqyhcr3IB9bTkUlI9xJ1MsN_foO2; wxa_level=1; retina=1; cid=9; wqmnx1=MDEyNjM2NTpkMWwwdWQ2ZSAvTmxpLkhsZUMvLm9TLzZGMm4tM1FVTyomSA%3D%3D; jxsid=17401873250460617876; appCode=ms0ca95114; webp=1; visitkey=8579849449254600101; __jdb=76161171.3.1090644581|15.1740187317; mba_muid=1090644581; mba_sid=17401873251726312719512330844.1; __jd_ref_cls=MDownLoadFloat_ApiDownloadAppPlugInOpenApp; cd_eid=jdd03GVTB6UHAPJLV2ZFD55FZO2A24P3VUF7EFNYXPRZSNWF37LC542XP6T4CXSVJIN7Y6KZE4GCTWQTHXELQJDJF4QVHWIAAAAMVFM7TJSIAAAAAC22WJKWAIWGI6MX"
           }

response = requests.post(url=url, headers=headers)
print(response.text)
