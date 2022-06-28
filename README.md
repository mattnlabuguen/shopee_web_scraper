# shopee_web_scraper
Python script that scrapes Shopee information

# How to use

Just paste a Shopee URL into the command line when prompted

It will output a .json file like this:

```
{
    "price": {
        "source": "<div class=\"pmmxKx\">₱599 - ₱799</div>",
        "value": "₱599"
    },
    "currency": {
        "source": "<div class=\"pmmxKx\">₱599 - ₱799</div>",
        "value": "₱"
    },
    "stock": {
        "source": "[<div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Category</label><div class=\"flex items-center ezgp+5\"><a class=\"ClhheV _3D+ogo\" href=\"/\">Shopee</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Audio-cat.11115519\">Audio</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Earphones-Headphones-Headsets-cat.11115519.11115539\">Earphones, Headphones &amp; Headsets</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Gaming-Headsets-cat.11115519.11115539.11021190\">Gaming Headsets</a></div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Brand</label><a class=\"kQy1zo\" href=\"/search?brands=1695333\">Misodiko</a></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Connection Type</label><div>Wired</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Earphone, Headphone, &amp; Headset Type</label><div>Over Ear</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Gaming Focused</label><div>Yes</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Audio Compatibility</label><div>Mobile, PC &amp; Laptop</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Headphone Accessory Type</label><div>Earpads</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Stock</label><div>3997</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Ships From</label><div>Mainland China</div></div>]",
        "value": {
            "Stock": "3997"
        }
    },
    "description": {
        "source": "<p class=\"hrQhmh\">Compatible with (but not limited to):\nLogitech G633 (G635/ G633S), G933 (G935/ G933S), G930, G430, G230, G231, G331, G431, G332, G432, G433, G533 Gaming Headset.\n\n-------------------------------------------------\n\nPackage include: 1-Pair Earpads (Not include any headphones).\nBrand name: misodiko\n\n--------------------------------------------------\n\nMust read before you buy:\nmisodiko's upgraded series earpads are significantly thicker than the original ones\nin order to make it more comfortable to wear for long periods of time.\nAnd they will also change the sound by increasing the distance between your ears and the drivers.\nSome people like this change and some people don't. This is a subjective feeling.\nIn short, if you don't want the earpads change the sound in any way, please don't buy it.</p>",
        "value": "Compatible with (but not limited to):\nLogitech G633 (G635/ G633S), G933 (G935/ G933S), G930, G430, G230, G231, G331, G431, G332, G432, G433, G533 Gaming Headset.\n\n-------------------------------------------------\n\nPackage include: 1-Pair Earpads (Not include any headphones).\nBrand name: misodiko\n\n--------------------------------------------------\n\nMust read before you buy:\nmisodiko's upgraded series earpads are significantly thicker than the original ones\nin order to make it more comfortable to wear for long periods of time.\nAnd they will also change the sound by increasing the distance between your ears and the drivers.\nSome people like this change and some people don't. This is a subjective feeling.\nIn short, if you don't want the earpads change the sound in any way, please don't buy it."
    },
    "specifications": {
        "source": "[<div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Category</label><div class=\"flex items-center ezgp+5\"><a class=\"ClhheV _3D+ogo\" href=\"/\">Shopee</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Audio-cat.11115519\">Audio</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Earphones-Headphones-Headsets-cat.11115519.11115539\">Earphones, Headphones &amp; Headsets</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Gaming-Headsets-cat.11115519.11115539.11021190\">Gaming Headsets</a></div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Brand</label><a class=\"kQy1zo\" href=\"/search?brands=1695333\">Misodiko</a></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Connection Type</label><div>Wired</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Earphone, Headphone, &amp; Headset Type</label><div>Over Ear</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Gaming Focused</label><div>Yes</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Audio Compatibility</label><div>Mobile, PC &amp; Laptop</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Headphone Accessory Type</label><div>Earpads</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Stock</label><div>3997</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Ships From</label><div>Mainland China</div></div>]",
        "value": {
            "Category": "Gaming Headsets",
            "Connection Type": "Wired",
            "Earphone, Headphone, & Headset Type": "Over Ear",
            "Gaming Focused": "Yes",
            "Audio Compatibility": "Mobile, PC & Laptop",
            "Headphone Accessory Type": "Earpads",
            "Ships From": "Mainland China"
        }
    },
    "brand": {
        "source": "[<div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Category</label><div class=\"flex items-center ezgp+5\"><a class=\"ClhheV _3D+ogo\" href=\"/\">Shopee</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Audio-cat.11115519\">Audio</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Earphones-Headphones-Headsets-cat.11115519.11115539\">Earphones, Headphones &amp; Headsets</a><svg class=\"shopee-svg-icon IJzbFa icon-arrow-right\" enable-background=\"new 0 0 11 11\" viewbox=\"0 0 11 11\" x=\"0\" y=\"0\"><path d=\"m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z\"></path></svg><a class=\"ClhheV _3D+ogo\" href=\"/Gaming-Headsets-cat.11115519.11115539.11021190\">Gaming Headsets</a></div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Brand</label><a class=\"kQy1zo\" href=\"/search?brands=1695333\">Misodiko</a></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Connection Type</label><div>Wired</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Earphone, Headphone, &amp; Headset Type</label><div>Over Ear</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Gaming Focused</label><div>Yes</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Audio Compatibility</label><div>Mobile, PC &amp; Laptop</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Headphone Accessory Type</label><div>Earpads</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Stock</label><div>3997</div></div>, <div class=\"_3Xk7SJ\"><label class=\"UWd0h4\">Ships From</label><div>Mainland China</div></div>]",
        "value": "Misodiko"
    },
    "delivery": {
        "source": "<div class=\"_1XIpMC\">Receive by 4 - 11 Jul</div>",
        "value": "Receive by 4 - 11 Jul"
    },
    "shipping": {
        "source": "<div class=\"tKRqjN\">₱0</div>",
        "value": "₱0"
    },
    "img_urls": {
        "source": "[<div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/0e0917cc511fe8a6dbd5bb1c55aad62e_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/4ef648a09d80108102ab6ac650b3adff_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/12345d70848ef92b40804eac8b8f68f7_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/4d43bd28a970915dd18e61d5f02db370_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/a3817cc150fd4592db86d588c3161702_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/28871b0b0a793a182e4e985b74033825_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/99a948102f15f1a75628c6391a37f075_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/bd3f80344f480c11aabcf85b598abc3c_tn\"); background-size: contain; background-repeat: no-repeat;'></div>, <div class=\"agPpyA _8akja2\" style='background-image: url(\"https://cf.shopee.ph/file/2fd18857e08cc76a50f3933c231367ba_tn\"); background-size: contain; background-repeat: no-repeat;'></div>]",
        "value": [
            "https://cf.shopee.ph/file/0e0917cc511fe8a6dbd5bb1c55aad62e",
            "https://cf.shopee.ph/file/4ef648a09d80108102ab6ac650b3adff",
            "https://cf.shopee.ph/file/12345d70848ef92b40804eac8b8f68f7",
            "https://cf.shopee.ph/file/4d43bd28a970915dd18e61d5f02db370",
            "https://cf.shopee.ph/file/a3817cc150fd4592db86d588c3161702",
            "https://cf.shopee.ph/file/28871b0b0a793a182e4e985b74033825",
            "https://cf.shopee.ph/file/99a948102f15f1a75628c6391a37f075",
            "https://cf.shopee.ph/file/bd3f80344f480c11aabcf85b598abc3c",
            "https://cf.shopee.ph/file/2fd18857e08cc76a50f3933c231367ba"
        ]
    },
    "vid_urls": {
        "source": "",
        "value": []
    }
}
```
