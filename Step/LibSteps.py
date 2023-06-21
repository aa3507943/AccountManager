from Step.StepGoogle import StepGoogle
from Step.StepMVBcom import StepMVBcom
from Step.StepTW import TWSteps
from Driver.web_control import WebControl
from Element.LibElements import AllElements


class AllSteps:
    def __init__(self, driver: WebControl, element: AllElements):
        self.G_Step = StepGoogle(driver, element)
        self.MVB_Step = StepMVBcom(driver, element)
        self.TW_Step = TWSteps (driver, element)