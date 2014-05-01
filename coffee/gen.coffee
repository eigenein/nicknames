
gen = (model, length) ->
  word = "$$"

  loop

    if word.length >= length and word.slice(-2) in model.breakable
      break

    entries = model.p[word.slice(-2)]
    if not entries
      break

    r = Math.random()
    for entry in entries
      [char, p] = entry
      if r < p
        word += char
        break

  word = word.replace(/\$/g, "")

this.gen = gen  # DEBUG
