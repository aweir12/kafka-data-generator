# kafka-data-generator
Simple Python script to generate data and produce Kafka messages

<h2>Overview</h2>
<p>This is a simple python script to generate a number of pseudo random integers and send the messages to a Kafka topic.</p>

<h3>Default Values</h3>
<p>By default the script will generate 25 random integers between the values of 0 and 25.</p>


<h3>Default Override</h3>
<p>You can override the default values by setting the variables numsToGen, minNumToGen, maxNumToGen. Alternatively, you can set the takeInput variable to the value of 'Y' to prompt for user input at runtime.</p>
