
var original_phase = "that is a good script"
var phrase = original_phase.split(" ")

function dopify(text){
	var new_phrase = []
	for (var i=0; i < text.length; i++){
		if (dictionary[text[i]]){
			slang_results = dictionary[text[i]];
			var slang_word = slang_results[Math.floor(Math.random()*new_phrase.length)];
			new_phrase.push(slang_word);
		}
		else {
			new_phrase.push(text[i]);
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

dopify(words)