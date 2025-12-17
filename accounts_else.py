from loguru import logger
import json


# built_up_file = {
#     'eg1':'eg2'
# }
# json_format = json.dumps(built_up_file)
# with open('built_up_account_message.json','wb') as f:
#     f.write(json_format.encode('utf-8'))


# correct_answer = {
#     'result' : 'correct'
# }
# with open('whether_check_correct.json','wb') as wf:
#     wf.write(json.dumps(correct_answer).encode('utf-8'))


def vocabulary_tool_add_account(name ,code):
    logger.info('vocabulary_tool_add_account running...')
    try:
        if code is None or len(code) == 0:
            logger.error('code is none ...')
            return

        elif name is None or len(name) == 0:
            logger.error('name is none ...')
            return

        with open('built_up_account_message.json', 'rb') as f:
            content = json.load(f)
            content[name] = code
            with open('built_up_account_message.json', 'wb') as rf:
                rf.write(json.dumps(content).encode('utf-8'))
            logger.info('account message saved..')
            return

    except Exception as e:
        logger.error(e)
        return

# vocabulary_tool_add_account(name='a1',code='a1')

def vocabulary_tool_check_account(verify_name ,verify_code):
    logger.info('vocabulary_tool_check_account running...')
    try:
        if verify_name is None or len(verify_name) == 0:
            logger.error('verify_name is none ...')
            return
        elif verify_code is None or len(verify_code) == 0:
            logger.error('verify_code is none ...')
            return

        with open('built_up_account_message.json', 'rb') as cf:
            check_content = json.load(cf)
            print(check_content)
            if check_content[verify_name] == verify_code:
                correct_answer = {
                    'result' : 'correct'
                }

                with open('whether_check_correct.json' ,'wb') as wf:
                    wf.write(json.dumps(correct_answer).encode('utf-8'))
            #
            elif check_content[verify_name] != verify_code:
                wrong_answer = {
                    'result' : 'wrong'
                }
                with open('whether_check_correct.json' ,'wb') as wf:
                    wf.write(json.dumps(wrong_answer).encode('utf-8'))

            else:
                logger.info('some conditions arise....')
                return

    except Exception as e:
        logger.error(e)

# vocabulary_tool_check_account(verify_name='eg1',verify_code='eee')