text = "This is a test script"

var words = ["this", "is", "a", "test", "script"]

function match(text){

	for (var i=0; i<words.length; i++){
		if (dictionary.words[i]){
			console.log(dictionary.words[i])
		}
	}

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


match(words)