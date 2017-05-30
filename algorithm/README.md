algorithm
=====

The algorithm has been created with the [Orange](https://orange.biolab.si/) version 3.41 CN2 classifier. There are two versions of the algorithm available: v2, based on the original plan, and the improved v3. The v3 has more rich column data values and has difficulty removed to decrease the number of columns.

List of files
----
* ruleset_human_readable.[xlsx,ods,csv] - the sample ruleset in a human readable format
* training_set_cleaned.[xlsx,ods,csv] - training set for the Orange CN2 classifier
* modelfile_v[2,3].pkcls - the sample classifier, created with Orange's CN2 classifier
* ludusdomain.pkl - domain file for the sample classifier, for v2 iteration
* docs - output report from Orange classification process and the CN2 classifier parameters

Please note the the csv-files are in European format (semicolon-separated values).

Some more important variables
----

| Variable               	| Variable name in code 	| Source        	|                                         	|
|------------------------	|-----------------------	|---------------	|-----------------------------------------	|
| Hexad type             	| hexad                 	| Questionnaire 	|                                         	|
| User skill             	| userskill             	| Self-rated    	|                                         	|
| Other user skill       	| otherskill            	| Self-rated    	|                                         	|
| Own team status        	| ownteam opentasks     	| Detected      	|                                         	|
| Avg. task age          	| ownteam taskage       	| Detected      	|                                         	|
| Other team task status 	| otherteam opentasks   	| Detected      	|                                         	|
| Chat activity level    	| chatactivity          	| Detected      	| Note: Merged with questionsinchat in v3 	|
| Questions in chat      	| questionsinchat       	| Detected      	| Note: Merged with chatactivity in v3    	|
| User points            	| ownpoints             	| Detected      	|                                         	|
| Other teams' points    	| otherteampoints       	| Detected      	|                                         	|
| Has helped others      	| hashelped             	| Detected      	| Note: Removed in v3                     	|
