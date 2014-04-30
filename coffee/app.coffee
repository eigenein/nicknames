
$ ->
  window.live = $("#live")
  window.last = $("#last")
  $("#btn-gen").on("click", update_nickname)
  update_live()

update_recent = (el, item) ->
  $("<li>#{item}</li>")
    .hide()
    .css("opacity", 0.0)
    .prependTo(el)
    .slideDown("slow")
    .animate({opacity: 1.0})

update_live = ->
  console.log("Live.")
  update_recent(live, gen())
  setTimeout(update_live, 200 + 2000 * Math.random())

update_nickname = ->
  el = $("#nickname")
  nickname = gen()
  el.text(nickname)
  update_recent(last, nickname)
