
# using vars: install_filter

label start:
	play music music_list['usual'] fadein 1
	scene bg city-1 with dissolve
	
	"Я стоял возле перилл над обрывом и наслаждался видом города."
	"Своего города, между прочим!"
	"Ведь это я управлял его жизнью уже больше 10 лет и улучшал тут всё как мог."
	
	play sound sfx_list['knock']
	snd "Тук-тук."
	"Я услышал какой-то стук."
	"Оглянувшись по сторонам, я не заметил ничего и никого необычного."
	play sound sfx_list['knock']
	snd "Тук-тук!"
	"Этот звук шёл словно со всех сторон сразу и даже не думал прекращаться."
	play sound sfx_list['knock']
	pause 0.5
	play sound sfx_list['knock']
	snd "Тук-тук-тук-тук!"
	"Что бы это могло быть, и что бы это могло значить?!"
	"..."
	stop music fadeout 2
	"Нет! {w}Только не это! {w} Только не сейчас!"
	
	scene bg my_room with dissolve
	"Я проснулся от того, что кто-то с большим упорством стучался в дверь моей комнаты"
	play music music_list['usual'] fadein 1
	me "Рен, блин, ну сколько можно-то уже! 15 лет жизни прожито теперь зря!"
	"Я поднялся и открыл дверь сестре."
	
	show rn normal with dissolve
	rn "15? Да ладно тебе. {w=1}Не поверю, что б ты так долго не сохранялся."
	rn "А даже если это и так, то всё равно автосохранения есть, так что не переживай: максимум последний год придётся переигрывать."
	rn "И вообще, хватит делать вид, будто в реальности за время твоего сна прошло больше 6 часов..."
	
	me "Ну, так-то оно так, но всё равно неприятно, когда тебя отвлекают."
	me "Вот возьму и не свожу тебя в свой сон за такое...чего пришла-то?"
	
	show rn happy with dissolve
	rn "Я проснулась пару часов назад и услышала по местным новостям о конкурсе художников!"
	me "Ну и скукотища."
	"Сказал я и всем видом показал, что если это всё - она вполне может быть свободна."
	rn "Да ты же о призах не слышал!"
	rn "Первое место - новый космический корабль, второе - куча бесплатных ремонтов, третье -..."
	me "Ясно-ясно. {w}Дай угадаю: ты хочешь в этом участвовать, и нам придётся на пару недель остаться в этой системе?"
	
	show rn serious with dissolve
	rn "К сожалению, не совсем так."
	rn "На конкурс действительно было отведено 2 недели, но я услышала о нём только сейчас, когда сообщили, что он заканчивается через 2 дня."
	me "2 дня? {w}Я нисколько не сомневаюсь в твоих талантах, но разве можно за такое короткое время нарисовать что-нибудь стоящее?"
	show rn normal with dspr
	rn "Разумеется, да! {w=1}Особенно, если случайно начать рисовать заранее кое-что похожее..."
	me "Так вот оно что."
	rn "Мы же останемся, да? {w=1}Скажи <да>, скажи-скажи-скажи..."
	
	menu:
		"Да":
			me "Ладно, 2 дня мы вполне можем пробыть и здесь."
			show rn happy with dspr
			rn "Ура-ура!"
			hide rn with dspr
			"Сказала она радостная и убежала, крикнув по пути:"
			rn "Кстати, завтрак тебе приготовлен!"
			"Ну, хоть одна хорошая новость на утро..."
			"..."
			$ days += 2
			"Мы провисели на орбите 2 дня."
			$ days += 1
			"И ещё день ждали подведения итогов."
			"По которым сестра заняла 7-е место из нескольких десятков тысяч."
			"Вполне неплохо, конечно. {w}Но если б она рисовала с самого начала, то могла бы и лучше..."
			
			show rn normal with dissolve
			me "Так что ты там о призах говорила?"
			rn "Как остаться - так тебя уговаривать надо, а как призы - так первым делом..."
			me "По-твоему, мне нужно было после окончания конкурса улететь и забыть об этом?"
			rn "Нет, но...короче, 7 место - это какая-то новейшая система очистки воды."
			me "Фи...И всего-то?"
			rn "Не всего-то! {w}Говорю же, супер новая, она во много раз эффективнее нашей, ест меньше энергии, лучше чистит, полностью автономна и стоит вообще-то кучу денег."
			me "Думаю, нам бы и нашей хватило."
			me "Мы вроде как и не собирались отфильтровывать воду из непонятных океанов с кислотой на первой попавшейся планете."
			me "Ну да ладно, если она ест меньше энергии и не требует ухода - это хорошо."
			
			$ install_filter = True
			
		"Нет":
			me "Ты издеваешься?"
			me "Только мы купили корабль и выбрались на орбиту, так тебе вдруг срочно понадобилось участвовать в конкурсе, который идёт уже больше недели."
			me "Где ты раньше-то была?!"
			show rn surprise with dissolve
			rn "Но я ведь...я ведь тоже не сидела на месте и кучу вещей готовила к переносу на корабль...и много с кем договаривалась...и..."
			me "И поэтому не могла выделить пару минут за всю неделю на то, что тебе интересно?"
			me "Не неси ерунды, если не интересовалась - значит не интересно."
			rn "Но..."
			me "Всё. Летим через 2 часа."
			
			hide rn with dissolve
			"Она ушла. {w}Обиженная и расстроенная. {w}Думаю, мне это ещё аукнется..."
			"Надо, конечно, быть с ней помягче, но почему же она такая рассеянная и всё делает в последний момент!"
			
			$ install_filter = False
	"..."
	jump main