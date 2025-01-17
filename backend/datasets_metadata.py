CHRISTMAS_QUESTIONS = {
    'Question 1'    : 'This Christmas how much money do you intend to spend in the following areas when compared to Christmas last year?',
    'Question 2'    : 'How frequently do you typically buy something that you didn’t plan to buy when shopping in a supermarket grocery store or off licence at Christmas time?',
    'Question 3'    : 'To what extent are the purchase decisions you make at Christmas in a supermarket grocery store or off licence impacted by the advertising you see?',
    'Question 4'    : 'How impactful or not are the following types of advertising campaigns on the purchases you make from a supermarket grocery store or off licence at Christmas time?',
    'Question 5'    : 'Top 3 favourite Brands to buy in a supermarket grocery store or off licence at Christmas time?',
    'Question 6'    : 'Which of the following types of media is most likely to get your attention when looking for brands to purchase at Christmas time?',
    'Question 7'    : 'what other types of media are likely to get your attention when looking for brands at Christmas time?'
}

CHRISTMAS_ANSWERS = {
    'Question 1'    : [['Food and Beverages',
                        'Beauty and Cosmetics',
                        'Health and Wellness',
                        'Fashion and Clothing',
                        'Socialising out of home e.g In Restaurants bars and cafes'],
                        ['More', 'Same', 'Less']],
    'Question 2'    : [['Always', 'Often', 'Sometimes', 'Rarely', 'Never']],
    'Question 3'    : [['Always', 'Often', 'Sometimes', 'Rarely', 'Never']],
    'Question 4'    : [['Celebrity endorsements',
                        'Health credentials',
                        'Humour',
                        'Occasion based messages (ideas for how and when I can use the product)',
                        'Old Fashioned values',
                        'Price cuts',
                        'Premium or Quality credentials',
                        'Sustainability',
                        'Tells me a story about the brand or product',
                        'Unique claims or brand attributes',
                        'Value deals or offers eg 2 for 1 offers'],
                        ['Very Impactful', 'Fairly Impactful', 'Neither', 'Not very impactful', 'Not at all impactful']],
    'Question 5'    : [['Denny’s', 'Jameson', 'M&S', 'Baileys', 'Coca Cola', 'Smirnoff',
                       'Tesco', 'Tayto', 'None', 'Dunnes Stores', 'Cadbury’s', 'Powers',
                       'Lindt', 'Ballymaloe', 'Heineken', 'Other Brands', 'Roses', 'Absolut',
                       'Guinness', 'Quality Street', 'No Group']],
    'Question 6'    : [['TV', 'Radio', 'Print media eg newspapers magazines flyers',
                       'Out of Home eg billboards posters', 'Tiktok', 'Twitter', 'Facebook', 'Instagram',
                       'General Online advertising', 'Email', 'Other']],
    'Question 7'    : [['TV', 'Radio', 'Print media eg newspapers magazines flyers',
                       'Out of Home eg billboards posters', 'Tiktok', 'Twitter', 'Facebook', 'Instagram',
                       'General Online advertising', 'Email', 'Other']],
}
CHRISTMAS_ANSWERS_LEVEL_NAMES = ['Consumer Area', 'Relative Spending']

CHRISTMAS_GROUPS = {
    'Sample'        : ['Total'],
    'Gender'        : ['Male', 'Female'],
    'Irish Region'  : ['Dublin', 'Leinster', 'Munster', 'Connacht', 'Ulster'],
    'Age Range'     : ['18 to 24', '25 to 34', '35 to 44', '45 to 54', '55 to 64'],
    'Question 2'    : CHRISTMAS_ANSWERS['Question 2'][0],
    'Question 3'    : CHRISTMAS_ANSWERS['Question 3'][0],
    'Question 5'    : CHRISTMAS_ANSWERS['Question 5'][0][:-1], # Exclude 'No Group' as answer (all zeros)
    'Question 6'    : CHRISTMAS_ANSWERS['Question 6'][0],
    'Question 7'    : CHRISTMAS_ANSWERS['Question 7'][0]
}
CHRISTMAS_GROUPS_LEVEL_NAMES = ['Criteria', 'Group']



SUSTAINABILITY_QUESTIONS = {
    'Question 1'    : 'Rank the importance of the following issues facing the UK today from 1 being the most important to 10 being of lesser importance.',
    'Question 2'    : 'Select which, if any, of the following most closely represents your dietary preference',
    'Question 3'    : 'How frequently or not would you say you purchase products that could be considered as environmentally friendly or sustainable?',
    'Question 4'    : 'In your opinion how important or not are the sustainability credentials of the brands or products that you buy?',
    'Question 5'    : 'What does the term sustainable mean to you?',
    'Question 6'    : 'How frequently do you engage in any of the following practices?',
    'Question 7'    : 'How frequently do you engage in any of the following practices?',
    'Question 8'    : 'Primarily who’s responsibility do you believe it is to drive sustainability practises or values in the UK?',
    'Question 9'    : 'To what extent do you trust companies and the messages they communicate based on being environmentally friendly or sustainable?',
    'Question 10'   : 'Which of the following types of claims by companies who produce consumer products do you find most impactful when choosing to purchase brands or products?',
    'Question 11'   : 'Which of the following claims do you find the most impactful when choosing to purchase brands or products from that company?',
    'Question 12'   : 'When shopping for items in store or online how influenced or not are you to make a purchase decision based on environmental or sustainable claims that appear on a products packaging?',
    'Question 13'   : 'In general how do you rate each of the following categories on their sustainability practices or values?',
    'Question 14'   : 'Rank the following categories from the one you feel is most sustainability focused (1) to the one you feel is least sustainability focused (5)',
    'Question 15'   : 'Have you ever stopped buying a brand or product for ethical or sustainability reasons?',
    'Question 16'   : 'Which category did the brand product belong to?',
    'Question 17'   : 'What was the reason you stopped buying this brand or product?',
    'Question 18'   : 'How much extra are you willing to pay for products in each of the following categories that are more environmentally conscious or engage in sustainable practices?',
    'Question 19'   : 'How much do you agree or disagree with the following statement? ‘The more expensive the brand or product, the more credible its sustainability claims are’',
    'Question 20'   : 'Name one brand that stands out to you for its environmental or sustainability focus.'
}

SUSTAINABILITY_ANSWERS = {
    'Question 1'     : [['Crime', 'Cost of Living', 'Education', 'Housing', 'International conflict',
                        'Mortgage interest rates', 'The economy', 'The environment and climate change',
                        'The NHS', 'Unemployment']],
    'Question 2'     : [['Vegetarian', 'Vegan', 'Pescatarian', 'Halal', 'Kosher', 'None of the above']],
    'Question 3'     : [['Always', 'Often', 'Sometimes', 'Rarely', 'Never']],
    'Question 4'     : [['Very important', 'Fairly important', 'Neither', 'Fairly unimportant', 'Very unimportant']],
    'Question 5'     : [['Environmentally Friendly', 'Good for the planet', 'Less waste', 'Local', 'Ethical',
                        'Dont know', 'Longer lasting', 'No natural resource depletion', 'Recyclable', 'Locally sourced',
                        'Zero carbon', 'Reuse or repurpose', 'None']],
    'Question 6'     : [['Check if products are made from recyclable or biodegradable materials',
                         'Limit my use of single use plastics',
                         'Pay more for a more durable or longer lasting items',
                         'Purchase fewer plastics',
                         'Purchase more locally produced goods',
                         'Purchase products made of natural ingredients',
                         'Purchase second-hand items'],
                        ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']],
    'Question 7'     : [['Purchase brands that promote environmentally sustainable practices or values',
                         'Recycle food waste',
                         'Recycle packaging waste',
                         'Repair or fix or upcycle items instead of replacing with a brand new version',
                         'Use public transport more frequently',
                         'Use fewer chemicals',
                         'Use renewable energy'],
                         ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']],
    'Question 8'     : [['The UK government ',
                        'Global corporations e.g the companies that own large well-known brands',
                        'Global agencies e.g WWF or Greenpeace or friends of the earth etc',
                        'All adults who live in the UK',
                        'All of the above']],
    'Question 9'     : [['Very much', 'Somewhat', 'Undecided', 'Not really', 'Not at all']],
    'Question 10'    : [['Minimising the consumption of products associated with deforestation and forest degradation',
                        'Donating a proportion of profits to environmental organisations',
                        'Implementing reduced waste goals',
                        'Partnering with local producers of materials',
                        'Planting trees to help protect the environment',
                        'Reducing greenhouse gas emissions',
                        'Reducing production of plastic packaging',
                        'Sourcing renewable or ‘green’ energy for production',
                        'Using biofuels',
                        'Using certified ‘sustainable’ materials in production',
                        'None of the above']],
    'Question 11'    : [['Minimising the consumption of products associated with deforestation and forest degradation',
                        'Donating a proportion of profits to environmental organisations',
                        'Implementing reduced waste goals',
                        'Partnering with local producers of materials',
                        'Planting trees to help protect the environment',
                        'Reducing greenhouse gas emissions',
                        'Reducing production of plastic packaging',
                        'Sourcing renewable or ‘green’ energy for production',
                        'Using biofuels',
                        'Using certified ‘sustainable’ materials in production',
                        'None of the above']],
    'Question 12'    : [['Very influenced', 'Fairly influenced', 'Neither', 'Not very influenced', 'Not at all influenced']],
    'Question 13'    : [['Food and Beverages',
                        'Health and Beauty and Cosmetics',
                        'Household Goods',
                        'Fashion and Clothing',
                        'Computers and Consumer Electronics'],
                        ['Excellent', 'Good', 'Fair', 'Poor', 'Very Poor']],
    'Question 14'    : [['Food and Beverages',
                        'Health and Beauty and Cosmetics',
                        'Household Goods',
                        'Fashion and Clothing',
                        'Computers and Consumer Electronics']],
    'Question 15'    : [['Yes', 'No', 'Do not know']],
    'Question 16'    : [['Food and Beverages',
                        'Health and Beauty and Cosmetics',
                        'Household Goods',
                        'Fashion and Clothing',
                        'Computers and Consumer Electronics',
                        'Other']],
    'Question 17'    : [['Use of Chemicals',
                        'Use of Palm Oil',
                        'Animal Testing',
                        'Ethical Concerns',
                        'Plastic Packaging',
                        'Renewable Resources',
                        'Environmental Impact',
                        'Sustainability',
                        'Unethical Practices',
                        'Supporting Genocide',
                        'Quality',
                        'Price',
                        'No Group']],
    'Question 18'    : [['Food and Beverages',
                        'Health and Beauty and Cosmetics',
                        'Household Goods',
                        'Fashion and Clothing',
                        'Computers and Consumer Electronics'],
                        ['Up to 5% more',
                         'Up to 10% more',
                         'Up to 20% more',
                         'Up to 30% more',
                         'Over 30% more',
                         'Nothing more']],
    'Question 19'    : [['Strongly Agree', 'Slightly Agree', 'Neither', 'Slightly Disagree', 'Strongly Disagree']],
    'Question 20'    : [['Amazon', 'Smol', 'Coca Cola', 'Patagonia', 'The Body Shop', 'Apple', 'Lush', 'Lidl', 'Ecover',
                        'Oceansaver', 'Tesco', 'No or do not know', 'Tesla', 'Nike', 'No Group']]
}
SUSTAINABILITY_ANSWERS_LEVEL_NAMES = ['Consumer Area', 'Relative Spending']

SUSTAINABILITY_GROUPS = {
    'Sample'        : ['Total'],
    'Gender'        : ['Male', 'Female'],
    'UK County'     : ['North East', 'North West', 'Yorkshire & The Humber', 'East Midlands', 'West Midlands',
                       'East of England', 'London', 'South East', 'South West', 'Wales', 'Scotland', 'Northern Ireland'],
    'Age Range'     : ['18 to 24', '25 to 34', '35 to 44', '45 to 54', '55 to 64'],
    'Question 2'    : SUSTAINABILITY_ANSWERS['Question 2'][0],
    'Question 3'    : SUSTAINABILITY_ANSWERS['Question 3'][0],
    'Question 4'    : SUSTAINABILITY_ANSWERS['Question 4'][0],
    'Question 5'    : SUSTAINABILITY_ANSWERS['Question 5'][0],
    'Question 8'    : SUSTAINABILITY_ANSWERS['Question 8'][0],
    'Question 9'    : SUSTAINABILITY_ANSWERS['Question 9'][0],
    'Question 10'   : SUSTAINABILITY_ANSWERS['Question 10'][0],
    'Question 11'   : SUSTAINABILITY_ANSWERS['Question 10'][0],
    'Question 12'   : SUSTAINABILITY_ANSWERS['Question 12'][0],
    'Question 15'   : SUSTAINABILITY_ANSWERS['Question 15'][0],
    'Question 16'   : SUSTAINABILITY_ANSWERS['Question 16'][0][:-1], # Exclude 'Other' as answer (all zeros)
    'Question 17'   : SUSTAINABILITY_ANSWERS['Question 17'][0],
    'Question 19'   : SUSTAINABILITY_ANSWERS['Question 19'][0],
    'Question 20'   : SUSTAINABILITY_ANSWERS['Question 20'][0],
}
SUSTAINABILITY_GROUPS_LEVEL_NAMES = ['Criteria', 'Group']


# General dicts containing all info
CHRISTMAS = {
    'PATH'                  : "christmas_dataset.xlsx",
    'DESCRIPTION'           : "Survey asking consumers in Ireland various questions to understand the consumers'"
                              "plans for Christmas, what their plans are overall and with spending.",
    'QUESTIONS'             : CHRISTMAS_QUESTIONS,
    'ANSWERS'               : CHRISTMAS_ANSWERS,
    'ANSWER_LEVEL_NAMES'    : CHRISTMAS_ANSWERS_LEVEL_NAMES,
    'GROUPS'                : CHRISTMAS_GROUPS,
    'GROUPS_LEVEL_NAMES'    : CHRISTMAS_GROUPS_LEVEL_NAMES
}
SUSTAINABILITY = {
    'PATH'                  : "sustainability_dataset.xlsx",
    'DESCRIPTION'           : "Survey asking consumers in the UK various questions around how important is"
                              "sustainability to consumers when they are buying products in general and"
                              "how engaged are consumers with sustainable brands or products.",
    'QUESTIONS'             : SUSTAINABILITY_QUESTIONS,
    'ANSWERS'               : SUSTAINABILITY_ANSWERS,
    'ANSWER_LEVEL_NAMES'    : SUSTAINABILITY_ANSWERS_LEVEL_NAMES,
    'GROUPS'                : SUSTAINABILITY_GROUPS,
    'GROUPS_LEVEL_NAMES'    : SUSTAINABILITY_GROUPS_LEVEL_NAMES
}