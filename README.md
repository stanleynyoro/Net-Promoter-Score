# Net Promoter Score with Python

Net Promoter Score (NPS) is an important indicator of customer loyalty. 
The higher the score, the greater the loyalty customers have towards a company, brand, service etc.

To come up with the score one need to ask a question-always framed as "“On a scale of 0 to 10, how likely are you to recommend [name of business] to a friend?”

- #Detractors, are those who give responses (0-6). They are not likely to recommend the company and worse, they are likely to a give a bad review.
- #Passives give responses (7-8).They are fence sitters who have not yet arrived at the decision of making recommendation
- #Promoters give responses (9-10). They wont hesitate in giving a recommendation.

We calculate NPS as #NPS=%#promoters-%#detractors.This implies that NPS can be negative a case in point, there are more detractors than promoters.

With NPS, companies can initiate strategies of how to retain promoters, win confidence of the passives. If the percentage of detractors is too high,
companies can strategise on how to best target the detractor market.

Further statistics could be performed with NPS, like crosstabulation of NPS by demographic variables such as gender, location, etc. Modelling the drivers of NPS could still be performed using logistic regression.

In my example, I have generated NPS of three companies i.e. A, B, C. The data used was generated through simulateing responses of 
387 cases. 
For the responses, I randomized responses (1-10) based on proportions. It is noted that this was necessary for if such was not done, 
it is highly likely that most responses would have been (0-6) i.e. detractors.
