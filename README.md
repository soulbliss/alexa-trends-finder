# alexa-trends-finder
Gather insights from the Alexa analytics website to see what is trending.

This is the root [Alexa webpage](https://www.alexa.com/topsites/category/Top) that this script can crawl within.



![](https://github.com/soulbliss/alexa-trends-finder/blob/master/img/Alexa-logo.jpg?raw=true)



#### So why was this made?

Being a inquisitive person and in college, I had to figure out what topics were trending in 

different domains like Science, Religion, Technology and set my future goals based on the insights 

gathered. But however there was a roadblock that I met, which was the costly API interface which Amazon 

offered. So to find a solution for that I created this script.



#### So What does this do?

For a given copied url of a certain topic like, let's say Science from one of these topics.

![](https://github.com/soulbliss/alexa-trends-finder/blob/master/img/alexa.png?raw=true)

It will give the below results. [ l - light analysis ]

![](https://github.com/soulbliss/alexa-trends-finder/blob/master/img/root.png?raw=true)

And here is the in depth version. [ d - in depth analysis]
![](https://github.com/soulbliss/alexa-trends-finder/blob/master/img/depth.png?raw=true)



#### So how to run this?

```
git clone https://github.com/soulbliss/alexa-trends-finder.git
cd alexa-trends-finder
pip install requirements.txt
cd alexa-trends-finder
#python3 core.py --help
```



**There are two ways to use this:**

1. If you have the url copied then.

```python
python core.py 
```



2. If you want to type the url then.

   ```python
   python core.py -u https://www.alexa.com/topsites/category/Top/News
   ```



### **Help output.**

```
Usage: core.py [OPTIONS]

Options:
  -u, --url TEXT          Accepts the url that needs to be digged. You can
                          have the link copied also.
  -o, --output_type TEXT  l for Light analysis, d for in depth analysis
  --help                  Show this message and exit.

```



The scraped folder contains the results for all major topics





#### Features to be worked on:

- [ ] Predict future trends using predictive modelling.
- [x] include the help argument handler.
- [ ] Smart crawling by limitting requests sent per second.
- [ ] Add the asciinema on the readme page.
