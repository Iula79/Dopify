function dopify(text){
	splitText = text.split(' ')
	var new_phrase = []
	for (var i=0; i < splitText.length; i++){
		if (dictionary[splitText[i]]){
			slang_results = dictionary[splitText[i]];
			var slang_word = slang_results[Math.floor(Math.random()*(new_phrase.length))];
			new_phrase.push(slang_word);
		}
		else {
			new_phrase.push(splitText[i]);
		}
	}
	return new_phrase
}

var dictionary = {
	"hello":["hiya", "yo"],
	"hi":["hiya", "yo"],
	"hey":["hiya", "yo"],
	"my name is":["they call me"],
	"how are you":["what up dawg", "wazzup homie"],
	"good":["sweet", "tight", "dope"],
	"fine":["just chillin'"],
	"very":["hella"],
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
