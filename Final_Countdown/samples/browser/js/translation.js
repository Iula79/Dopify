function dopify(text){
	splitText = text.split(' ')
	console.log(splitText)
	var new_phrase = []
	for (var i=0; i < splitText.length; i++){
		lowerCase = splitText[i].toLowerCase()
		if (dictionary[lowerCase]){
			slang_results = dictionary[lowerCase];
			var slang_word = slang_results[Math.floor(Math.random()*(dictionary[lowerCase].length))];
			console.log("This is slang word" + slang_word);
			new_phrase.push(slang_word);
		}
		else {
			new_phrase.push(splitText[i]);
		}
		
	}
	console.log("This is the new phrase" + new_phrase);
	return new_phrase
}

var dictionary = {
	"hello":["hiya", "yo"],
	"hi":["hiya", "yo"],
	"hey":["hiya", "yo"],
	"my name is":["they call me"],
	"how are you":["what up dawg", "wazzup homie"],
	"good":["sweet", "tight", "dope"],
	"fine":["just chillin'","gucci"],
	"very":["hella","mucho"],
	"really":["seriously", "literally"],
	"yes":["YAS", "hell yes"],
	"no":["hell no", "naww"],
	"haha":["LOL"],
	"hahaha": ["LMAO"],
	"the": ["da"],
	"that": ["dat"],
	"have": ["got"],
	"for": ["fo"]
}
