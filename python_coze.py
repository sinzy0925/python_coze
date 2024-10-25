import re
async def main(args: Args) -> Output:
    params = args.params
    posts = params["input"]
    expanded_urls = ""
    for post in posts:
        screen_name = post.get('user').get("screen_name")
        rest_id = post.get('rest_id')
        Text = post.get('full_text')
        #if params["SearchWord"] in Text:
        #if re.search(r'[ぁ-んァ-ンa-zA-Z]', Text):
        expanded_urls += "URL  : https://x.com/" + screen_name + "/status/" \
            + rest_id + "\nText : " + Text + "\n \n"

    ret: Output = {
        "key0": expanded_urls,
        "json_data": params["SearchWord"]#params,
    }
    return ret