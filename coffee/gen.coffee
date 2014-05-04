
gen = (model, length) ->
  word = Array(n).join("$")

  loop

    ending = word.slice(-n + 1)

    if word.length >= length and ending in model.breakable
      break

    entries = model.p[ending]
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
