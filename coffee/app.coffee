
$ ->
  window.n = 3
  window.models = models  # DEBUG
  window.recent =
    live: {el: $("#live"), counter: 0}
    last: {el: $("#last"), counter: 0}
  $("#btn-gen").on("click", update_nickname)
  update_nickname()
  update_live_once() for [1..40]
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
  # Update live with timeout.
  update_live_once()
  setTimeout(update_live, 200 + 2000 * Math.random())

update_live_once = ->
  update_recent(recent.live, gen(choose_model(), 6 + 8 * Math.random()))

update_nickname = ->
  # Update nickname field.
  el = $("#nickname")
  nickname = gen(choose_model(), 8)  # TODO
  el.text(nickname)
  update_recent(recent.last, nickname)

choose_model = (model_names) ->
  model_names = model_names or Object.keys(models)
  models[model_names[Math.floor(Math.random() * model_names.length)]]
