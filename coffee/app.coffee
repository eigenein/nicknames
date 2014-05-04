
$ ->
  # Models.
  window.n = 3
  window.models = models  # DEBUG
  # Cache elements.
  window.recent =
    live: {el: $("#live"), counter: 0}
    last: {el: $("#last"), counter: 0}
  # Set handlers.
  $("#btn-gen, #nickname").on("click", update_nickname)
  $("#nickname").mousedown((event) -> event.preventDefault())
  # Initialize controls.
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
  update_recent(
    recent.live
    gen(choose_model(), Math.floor(6 + 8 * Math.random()))
  )

update_nickname = ->
  # Update nickname field.
  length = parseInt($("input[name=nickname-length]:checked").val())
  name = $("input[name=nt]:checked").val()
  nickname = gen(models[name], length)
  $("#nickname").text(nickname)
  update_recent(recent.last, nickname)

choose_model = ->
  model_names = Object.keys(models)
  models[model_names[Math.floor(Math.random() * model_names.length)]]
