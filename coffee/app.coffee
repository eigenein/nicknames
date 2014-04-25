
$ ->
  console.log("Ready.")
  $("#btn-gen").on("click", update_nickname)
  update_live()

update_recent = (selector, item) ->
  $("<li>#{item}</li>")
    .hide()
    .css("opacity", 0.0)
    .prependTo(selector)
    .slideDown("slow")
    .animate({opacity: 1.0})

update_live = ->
  console.log("Live.")
  update_recent("#live", gen())
  setTimeout(update_live, 200 + 2000 * Math.random())

update_nickname = ->
  el = $("#nickname")
  nickname = gen()
  el.text(nickname)
  update_recent("#previous", nickname)
