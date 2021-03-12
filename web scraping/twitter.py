import twint
config = twint.Config()
#I ran the below code twice. First of all I searched for all tweets related to "whitehatjr" and then "whitehatjunior" and later removed dupliate values from dataset if any
config.Search="whitehatjr"
config.Since = "2020-08-27"
config.Store_csv = True
config.Output = "custom_twitter_data.csv"
twint.run.Search(config)
