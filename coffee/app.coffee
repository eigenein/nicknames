
$ ->
  window.models = models  # DEBUG
  for model of models
    console.log("Found model:", model)
  window.recent = {
    live: {el: $("#live"), counter: 0},
    last: {el: $("#last"), counter: 0},
  }
  $("#btn-gen").on("click", update_nickname)
  update_live()

update_recent = (object, item) ->
  # Prepend item.
  $("<li>#{item}</li>")
    .hide()
    .css("opacity", 0.0)
    .prependTo(object.el)
    .slideDown("slow")
    .animate({opacity: 1.0})
  # Limit items count.
  if object.counter > 50
    $(":last-child", object.el).remove()
  else
    object.counter += 1

update_live = ->
  update_recent(
    recent.live
    gen(
      models[Math.floor(Math.random() * models.length)]
      3 + 17 * Math.random()
    )
  )
  setTimeout(update_live, 200 + 2000 * Math.random())

update_nickname = ->
  el = $("#nickname")
  nickname = gen()
  el.text(nickname)
  update_recent(recent.last, nickname)
