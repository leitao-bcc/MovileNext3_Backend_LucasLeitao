from app.
from ..scheduled_jobs import app
import request


@app.route('/schedulePrint', methods=['POST'])
def schedule_to_print():
    data = request.get_json()
    #get time to schedule and text to print from the json
    time = data.get('time')
    text = data.get('text')
    #convert to datetime
    date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
    #schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
    job = scheduler.add_job(printing_something, trigger='date', next_run_time=str(date_time),
                            args=[text])
    return "job details: %s" % job