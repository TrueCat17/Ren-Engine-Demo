label ar_meet:
	scene bg buy_place-4 with dissolve
	"Недавно была обнаружена планета с алмазом вместо ядра."
	"Добывающая компания решила, что быстрее и проще всего будет послать в неё мощные ракеты, чтобы <смести> всё <лишнее>."
	"Потом они охладят полученное ядро, а затем просто будут откалывать от него сколько потребуется."
	"Я буду везти охлаждающее вещество в ту систему."	
	"Ну, учитывая необитаемость планеты и то, что в галактике их до сих пор даже подсчитать и сойтись на одной цифре не могут - во всём этом нет ничего такого."
	
	scene bg storage_planet with dissolve
	
	show ar angry at left with dissolve
	ar "Нет, она мне просто необходима! Выдайте!"
	$ set_random_trader()
	show trader at right with dissolve
	trader "Т. е. все прекрасно обходятся без охраны, а вы такая особенная?"
	trader "А в чём тогда вообще смысл вас нанимать, если у вас будет наше сопровождение?"
	trader "Проще тогда сразу самим всё перевезти."
	ar "Да что б я на это...{w=1} А хотя... Знаете что. Ладно. Я согласна."
	trader "Что-то быстро вы мнение своё поменяли."
	trader "Впрочем, не важно. Удачного полёта!"
	hide trader with dspr
	show ar serious at center
	ar "Огромное, блин, спасибо."
	
	"Сказала она уже после того, как он ушёл."
	me "Какие-то проблемы?"
	extend "Это ты перевозишь взрывчатку для ракет?"
	ar "Да. На оба вопроса да."
	