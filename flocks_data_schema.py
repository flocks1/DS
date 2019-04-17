# https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.to_json.html - orient:index
# https://docs.python.org/3/library/json.html - json.dumps()

# Data Schema Reference: Flocks


# tweet_id as df.index

# Tweets 
{
    tweets: # Used to render the tweets and sentiment for each.
    { 
        tweet_id: 902234038250284234,
        tweet_time: <timestamp> # May be needed for sorting
        tweet_sentiment:{
            is_angry: 1, # Binary, zero or one. Indicates whether sentiment was present or not in that tweet. 
            angry_value: 0.232,
            is_sad: 0, 
            sad_value: 0.232,
            is_happy: 1
            happy_value: 0.232,
            ...
            is_one_for_each_emojis: 0,
            one_for_each_emojis_value: 0.0023
        }
    },

    aggeragate_stats_table: # Use to make aggergate table. 
    {  
        overall_count: 100,
        overall_top_sentiment: "angry",
        overall_sentiments_detected: 42,
        overall_avg_sentiments_per_person: 3,
        earliest_time: <timestamp>, # Not displayed?
        most_recent_time: <timestamp>, # Not displayed? 
        sentiment_tables:# Icons displayed as ordered list above the stats grid. Click on emoji to see its agg stats. list of emoji id's. 
        {  
            angry: 1, # Binary, zero or one. Indicates whether sentiment was present or not in that tweet. 
            sentiment_0:{
                type: "angry",
                detected: True, # Flag whether to show the stat or not. 
                count: 8, # Number of comments sentiment was present in. 
                average: 0.999, # Average value of sentiment for that emoji.
                total_amt: 7.342 # Total scores of all tweets w/ that sentiment.
            },
            sentiment_1:{
                type: "sad",
                count: 3,
                average: .452
            }
            sentiment_n:{
                type: "sexually_explicit",
                detected: False, 
                count: 3,
                average: .452
            }
        }
    },

    
    timeseries_linegraph_object:{ # Use with recharts.org line chart. 
        {
            "period_label": "Oldest", # Could be a date or just text label. 
            "sentiment_0_period_avg": 0.65, # One value for each sentiment?
            "sentiment_1_period_avg": 0.85,
            "sentiment_3_period_avg": 0.74,
            ...
            "sentiment_n_period_avg": 0.10
        },
        {
            "period_label": "Newer",
            "sentiment_0_period_avg": 0.65,
            "sentiment_1_period_avg": 0.85,
            "sentiment_3_period_avg": 0.74,
            ...
            "sentiment_n_period_avg": 0.10
        },
        {
            "period_label": "Newest Period", 
            "sentiment_0_period_avg": 0.65,
            "sentiment_1_period_avg": 0.85,
            "sentiment_3_period_avg": 0.74,
            ...
            "sentiment_n_period_avg": 0.10
        },
    }

}








### Emojis to use ### 
["id",
        "comment_text",
        "target", # Toxic base. 😡 pouting face, Unicode: U+1F621, UTF-8: F0 9F 98 A1
        "severe_toxicity", # 🤬 face with symbols over mouth, Unicode: U+1F92C, UTF-8: F0 9F A4 AC
        "obscene",# 😳, face with wide open eyes, Unicode: U+1F633, UTF-8: F0 9F 98 B3
        "identity_attack", #🤥, lying face, Unicode: U+1F925, UTF-8: F0 9F A4 A5
        "insult", # 🖕 middle finger, Unicode: U+1F595, UTF-8: F0 9F 96 95
        "threat", # 👊, closed fist, Unicode: U+1F44A, UTF-8: F0 9F 91 8A
        "asian", # 👩🏻 woman, Unicode: U+1F469 U+1F3FB, UTF-8: F0 9F 91 A9 F0 9F 8F BB
        "atheist",# ⚛️ atom symbol, Unicode: U+269B U+FE0F, UTF-8: E2 9A 9B EF B8 8F
        "bisexual", # ⚥ MALE AND FEMALE SIGN, Unicode: U+26A5, UTF-8: E2 9A A5
        "black", # 👩🏿‍🦱, woman with curly hair, Unicode: U+1F469 U+1F3FF U+200D U+1F9B1, UTF-8: F0 9F 91 A9 F0 9F 8F BF E2 80 8D F0 9F A6 B1
        "buddhist",# ☸️, wheel of dharma, Unicode: U+2638 U+FE0F, UTF-8: E2 98 B8 EF B8 8F
        "christian",# ✝️, Latin cross, Unicode: U+271D U+FE0F, UTF-8: E2 9C 9D EF B8 8F
        "female",# ♀, FEMALE SIGN, Unicode: U+2640, UTF-8: E2 99 80
        "heterosexual",# ⚤ INTERLOCKED FEMALE AND MALE SIGN, Unicode: U+26A4, UTF-8: E2 9A A4
        "hindu",# 🕉, om symbol, Unicode: U+1F549, UTF-8: F0 9F 95 89
        "homosexual_gay_or_lesbian", # 🏳️‍🌈 rainbow flag Unicode: U+1F3F3 U+FE0F U+200D U+1F308, UTF-8: F0 9F 8F B3 EF B8 8F E2 80 8D F0 9F 8C 88
        "intellectual_or_learning_disability",# ♿️, wheelchair symbol, Unicode: U+267F U+FE0F, UTF-8: E2 99 BF EF B8 8F
        "jewish",# ✡️, Star of David, Unicode: U+2721 U+FE0F, UTF-8: E2 9C A1 EF B8 8F
        "latino",# 👩🏽 woman Unicode: U+1F469 U+1F3FD, UTF-8: F0 9F 91 A9 F0 9F 8F BD
        "male",# ♂, MALE SIGN, Unicode: U+2642, UTF-8: E2 99 82
        "muslim",# ☪️, star and crescent, Unicode: U+262A U+FE0F, UTF-8: E2 98 AA EF B8 8F
        "other_disability",# ♿️, wheelchair symbol, Unicode: U+267F U+FE0F, UTF-8: E2 99 BF EF B8 8F
        "other_gender",# ⚨, VERTICAL MALE WITH STROKE SIGN, Unicode: U+26A8, UTF-8: E2 9A A8
        "other_race_or_ethnicity",# 🌎, globe showing Americas, Unicode: U+1F30E, UTF-8: F0 9F 8C 8E
        "other_religion",# ☮️, peace symbol, Unicode: U+262E U+FE0F, UTF-8: E2 98 AE EF B8 8F
        "other_sexual_orientation",# ⚪, MEDIUM WHITE CIRCLE, Unicode: U+26AA, UTF-8: E2 9A AA
        "physical_disability",# ♿️, wheelchair symbol, Unicode: U+267F U+FE0F, UTF-8: E2 99 BF EF B8 8F
        "psychiatric_or_mental_illness",# 🤕, face with head-bandage, Unicode: U+1F915, UTF-8: F0 9F A4 95
        "transgender",# ⚧ MALE WITH STROKE AND MALE AND FEMALE SIGN, Unicode: U+26A7, UTF-8: E2 9A A7
        "white",# 👩🏼, woman, Unicode: U+1F469 U+1F3FC, UTF-8: F0 9F 91 A9 F0 9F 8F BC
        "funny",# 😆 grinning face with tightly closed eyes, Unicode: U+1F606, UTF-8: F0 9F 98 86
        "wow",# 😲 astonished face, Unicode: U+1F632, UTF-8: F0 9F 98 B2
        "sad",# 😢, crying face, Unicode: U+1F622, UTF-8: F0 9F 98 A2
        "likes", # 👍 thumbs up, Unicode: U+1F44D, UTF-8: F0 9F 91 8D
        "disagree",# 👎, thumbs down, Unicode: U+1F44E, UTF-8: F0 9F 91 8E
        "sexual_explicit" #🍆 eggplant Unicode: U+1F346, UTF-8: F0 9F 8D 86 
    ]