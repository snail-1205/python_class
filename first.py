# 파이썬은 너가 좋아하는 언어같은데 여기서 봇을 만들어본다면 어떨까..
# 못할거 뭐있겠어 한번 해보자~

from telegram.ext import Application ,CommandHandler, ContextTypes # telegram.ext라는 모듈에서 Application, CommandHandler을 가져온거임
from telegram import Update # 얘도 마찬가지

def main() -> None:
    """Run bot."""
    # 봇만드는거. 빌더패턴이라는 건데 요약하면 함수를 물고 물다가 마지막에 build(약속한말)로 완성시키는거임. 여기선 application을 완성시켰네
    application = Application.builder().token(
        "5797647402:AAEIiWXuhMttin44i6pIRozlDIJlnYqyXvk").build()
    
    # 이제 대답을 어떻게 하게 할거냐. 다 정해져 있지

    # application안에는 add_handler라는 함수가 있음. 이 함수는 배열을 받음.
    #무슨 배열이냐면 List[BaseHandler]라네? 이게 뭔말이냐면 ts에서 Array<BaseHandler>랑 똑같음, 파이썬에서 제너릭은 []로 표현함
    # 즉 배열 안에는 BaseHandler 타입을 가진 애들만 들어갈 수 있고 CommandHandler는 Basehandler에 속하나보네
    #CommmandHandler가 초록색인 이유 > 생성자 함수라서. js랑 똑같이 생각하면 됨. new가 사라졌을 뿐
    #CommandHandler의 생성자 함수는 인자를 두개를 받네. 하나는 명령할 말이고 다른 하나는 콜백함수
    #콜백함수 여기서도 또나오지? 모든 언어에 등장한다ㅋㅋ 
    #여기선 test라고 텔그로 메시지를 보내면 test 콜백함수를 실행하겠다는거임
    application.add_handlers([CommandHandler("test", test)]) 
    application.run_polling() # 기억날지 안날지 모르겠지만 polling이라는 말 js에도 있었음

# test 콜백함수가 없으니까 만들어주자.

def test(update : Update, context: ContextTypes.DEFAULT_TYPE): #타입넣는거 ts랑 비슷하지? 인자를 두개받는 useFunc에 넣을 콜백함수 기억해내면 됨
    update.message.reply_text("테스트하셨습니다.") #update안에있는 message안에있는 reply_text 함수를 호출(실행)한거

if __name__ == "__main__":
    main() # 이건 걍 실행한다는거






