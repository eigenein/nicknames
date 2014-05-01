
gen = (model, length) ->
  model = model or models["human-rus"]  # TODO
  length = length or 10  # TODO

  word = "$$"
  loop
    console.log("Current:", word)
    r = Math.random()
    for entry in model[word.slice(-2)]
      [char, p] = entry
      console.log("Trying:", char, p)
      if r < p
        word += char
        break
    break if word.slice(-1) == "$"

  word = word.replace(/\$/g, "")

this.gen = gen  # DEBUG
