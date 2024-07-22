from base.models import *
from datetime import datetime

def check_duedated_decrees():
    decrees = Decree.objects.filter(
        due_date__lte = datetime.now(), status = "received"
        )
    print(decrees)
    for decree in decrees:
        # get or created Fine object for this decree
        fine, is_created = Fine.objects.get_or_create(
            decree = decree, defaults={
                'staff': decree.receiver, 'date': datetime.now(),
                'fault': f"{decree.pk} - sonli buyruq o'z vaqtida bajarilmadi.",
            }
        )
    