from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import OiOrder,UiTeacher,UiStudent,OiClassCommonPolitic
from ky.api.base import Base



class Pol(Base):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        # 'order_id_fk':'order_id_fk',
        'class_level':'class_level',
        'teacher_name':'teacher_name',
        'assistant_name':'assistant_name',
        'skype_count':'skype_count',
        'skype_count_now':'skype_count_now',
        'fee':'fee',
        'if_protocol':'if_protocol',
        'create_time':'create_time',
        'update_time':'update_time'
    })




    def list(self):
        return OiClassCommonPolitic.objects.all()


    # 在order->sutdent 外建 这里id 逻辑上是学生id
    def detail(self, pk):
        order = OiOrder.objects.get(id=pk)
        return OiClassCommonPolitic.objects.get(order=order)

    def create(self):
        pass

    def update(self,pk):
        order = OiOrder.objects.get(id=pk)
        lesson = OiClassCommonPolitic.objects.filter(order=order)
        if not lesson.exists():
            lesson = OiClassCommonPolitic(order=order)
        else:
            lesson = OiClassCommonPolitic.objects.get(order=order)
        lesson.class_level = self.data['class_level'] if 'class_level' in self.data else lesson.class_level
        lesson.fee = self.data['fee'] if 'fee' in self.data else lesson.fee
        lesson.skype_count = self.data['skype_count'] if 'skype_count' in self.data else lesson.skype_count
        lesson.if_protocol = self.data['if_protocol'] if 'if_protocol' in self.data else lesson.if_protocol
        lesson.save()
        return lesson

    def delete(self, pk):
        pass