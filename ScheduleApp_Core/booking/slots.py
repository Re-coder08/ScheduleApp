
from accounts.models import Staff, Customer, CustomerProfile, StaffProfile
from booking.models import Booking

from datetime import time, datetime, timedelta

# need to add the end time also for better implementations on feature.
def add_duration_to_date(request, start_tm, add_dur):
    # print("add duration data  ::: {0},, {1}".format(start_tm, add_dur))
    placeholder_dt = datetime.fromisoformat('9999-01-01')
    append_tm = datetime.combine(placeholder_dt, start_tm[0]) + timedelta(hours=add_dur.hour, minutes=add_dur.minute)
    # print("after time  ::: {0},, {1}".format(start_tm, append_tm))
    
    return (append_tm.time(), )  

def GetAllSlots(request, staff_id, booking_date, duration):
        
        start_tm = StaffProfile.objects.filter(user_id = int(staff_id)).all().values_list('staff_start_time')[0]
        end_tm = StaffProfile.objects.filter(user_id = int(staff_id)).all().values_list('staff_end_time')[0]
        # print("All data : {}".format((request, staff_id, start_tm[0], str(start_tm[0]), str(end_tm[0]))))

        slots = []
        add_dur = duration
        if duration == '60':
            add_dur = time.fromisoformat('01:00:00')
        if duration == '30' or duration == None:
            add_dur = time.fromisoformat('00:30:00')

        slt_start_tm = start_tm

        while slt_start_tm[0] < end_tm[0]:
            slt_end_tm = add_duration_to_date(request, slt_start_tm, add_dur)
            # print(start_tm[0], end_tm[0])
            slots.append((slt_start_tm[0], slt_end_tm[0]))
            slt_start_tm = slt_end_tm

        slots = [ i for i in slots]
        # print("here : {}".format(slots))
        return slots

def GetAllBookedSlots(request, staff_user, booking_date, duration):
    #  print(type(staff_user))
     BookedSlots = Booking.objects.filter(staff_id = int(staff_user)).all().values_list('start_time', 'end_time')
     print("================>>>>>>")
     print("Booked Slots : {0} ".format(BookedSlots))
     return BookedSlots

def CheckOverlapSlots(request, all_slots, booked_slots):
    result = []
    for sl1_strt, sl1_end in all_slots:
        # print("top layer :: {}".format((sl1_strt, sl1_end)))
        
        for sl2_strt, sl2_end in booked_slots:
            sl2_strt = sl2_strt.time()
            sl2_end = sl2_end.time()
            # print("bottom layer :: {}".format((sl2_strt, sl2_end)))
            
            overlap = (sl1_strt < sl2_end) and (sl2_strt < sl1_end)
            if overlap :
                # remove.append((sl1_strt, sl1_end))
                print("----->>> remove : {}".format((sl1_strt, sl1_end)))
                result.append((sl1_strt, sl1_end))
            # print([sl1_strt, sl1_end,sl2_strt, sl2_end, overlap])

    final_slots = []
    for i in range(len(all_slots)):
        flag = True
        for x in range(len(result)):
            if all_slots[i] == result[x]:
                flag = False
        if flag == True:
            final_slots.append(all_slots[i])

    
            
                
    print("length of all slots {}".format(len(all_slots)))    
    print("length of overlap slots {}".format(len(result)))
    print("length of final slots {}".format(len(final_slots)))
   
    return sorted(final_slots)
            

def GenOptionTags(request, slots):
    result = []
    for i in slots:
        tgt = '<option value="{0}">{1}</option>'.format(i[0], i[1])
        result.append(tgt)
    return result