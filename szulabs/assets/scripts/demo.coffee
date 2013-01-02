  $ ->
  # we're using coffeescript
  # you could learn more from the Internet
  
  # this line will be print to the console of your browser
  console.log "hello, world"

  # set the todo tips
  $("ul li").each (i, element) ->
    $(element).text (j, text) -> "#{text} [@todo/#{i}]"
    $(element).attr
      class: "nav-item todo-#{i}",
      id: "nav-item-#{i}"
