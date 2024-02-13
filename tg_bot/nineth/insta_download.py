import requests


async def insta_video(link):
	url = "https://instagram-post-and-reels-downloader.p.rapidapi.com/insta/"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "81fb8ab861mshab3f38210b29688p1d13bfjsn2a09fbd6b61c",
		"X-RapidAPI-Host": "instagram-post-and-reels-downloader.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	data = response.json()
	video = data['detail']['data']['items'][0]['urls'][0]['url']

	return video
