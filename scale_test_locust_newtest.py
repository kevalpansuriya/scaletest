from locust import User, TaskSet, HttpUser, between, task



class WebsiteTasks(HttpUser):

    url = "https://ficcibike.com/maritime/"
    wait_time = between(3, 7)

    def on_start(self):
        self.host = "http://vapt.ficci.in"

    @task
    def login(self):


        self.client.get("allybooklaunch/index.php")
        self.client.post("allybooklaunch/data/loginData.phppasswd=&emailid=vandana.a.gupta%40accenture.com&g-recaptcha-response=03AGdBq25YnNighzXxxByLrkgkFCLng6Ex03mnmBEOgp8q_0RhkT8pB3yeSWzYPPKKnxZbSElcBu-QkjYLQH4p6jmg1pKcQ8nkdXFq9nU-9nprkEE2d2JVYfFtZ1zEc_5O0PRnkO7sUsTi3bbhx1yaP6a39bhsznxeDTfNFsTudfCOmpoQ6XUVhs23mn-OPGlqn69kLGql7ge6nqBseqhMrH3lnivn-0qdLXNVV7pe8-uxlcYNXTvjZcxDNGykvBz72cVrhNasNSkwBW82Uz9Ot0WE7iKOQq-wRP25nLMx892uSKc39buITQlCXYkeqb9NJV0SWV9S0LwkF5QjErS4Fia0nuKRjBLgP4Pn2VqolXMrdDcBKSLoHpNcMGRSqeMyzhvD2XebVWqgdXC3_2SjRHIv4k1DA497jIRB34k9vjjX3Yqv2ufOPhaW7k3IwC9ng11NcaNgnV7Hhxk7pGszJK2Hi2xZvgE_7A&action=validate_captcha")
        self.client.get("allybooklaunch/lobby.php")
        self.client.get("allybooklaunch/auditorium.php")






        # self.client.get("maritime/assets/images/login-back.png")
        # self.client.get("maritime/assets/images/ico.png")
        # self.client.get("maritime/assets/images/registation_video.mp4")
        # self.client.get("maritime/assets/css/style.css?v=1616739232")
        # self.client.get("maritime/assets/css/fontawesome470/css/font-awesome.min.css")
        # self.client.get("maritime/assets/images/title.jpg")
        # self.client.get("maritime/assets/images/close.png")
        #
        # payload = 'passwd=&emailid=keval_test&g-recaptcha-response=03AGdBq24wY4dF_KLNJJo9ku3Dq-ggf6lljy_HP1dZSBbxRn5MZSc5HjJslvgYGJJoc5UFSmMpTS-QrzBkeXGYf8qtxAdPmT9saOr4IezVTrSJqJB8MBEk8fyoLpzHXHUpEP7MHjnWdPz8yvp5Pgc8_qZZ3ejUeLqeFbB89SThKFtlv-2K2gcX7CiJzf59K_uevzBiCIfkRGSw3PVWKkD1ma7HCeUuYkQGNq8nwk5yMpKRh18ZZJvi_SUkYUGmsZyOM4fnMHTDMA-YyLjJdPok9aaSInq8ELvY_6wt1EHvliigwSE05-7jOObldNGp_yFZo7_hW1m9Iw5mNZt8XoSHdaVF5sSG1gtXj05neWYwo4vlD4BvDiXB0Q9SG2RmuolgkbdlvJ_yufQPIhLxX6JbdA167b8otRrouIkBW2cb4SbKsAHRIEXCHsS7IX7klw-Np1aG7iGcnjbw&action=validate_captcha'
        # headers = {
        #     'Content-Type': 'application/x-www-form-urlencoded',
        #     'Cookie': 'PHPSESSID=6cf86df6f057664ae8e20928991845a0'
        # }
        #
        # self.client.post("maritime/data/loginData.php",headers = headers,data=payload)
        #
        #
        # self.client.get("maritime/lobby.php")
        # self.client.get("maritime/assets/images/ficci.png")
        # self.client.get("maritime/assets/images/user.png")
        #
        # self.client.get("maritime/assets/css/style.css?v=1617181381")
        # self.client.get("maritime/assets/css/fontawesome470/css/font-awesome.min.css")
        # self.client.get("maritime/assets/images/title.jpg")
        #
        #
        # self.client.get("maritime/assets/images/close.png")
        # self.client.get("maritime/aun-new1.gif")
        # self.client.get("maritime/assets/js/jquery-3.4.1.min.js")
        #
        # self.client.get("maritime/assets/js/popper.min.js")
        # self.client.get("maritime/assets/js/bootstrap.min.js")
        # self.client.get("maritime/assets/js/mdb.min.js")
        # self.client.get("maritime/assets/js/jquery.validationEngine.js")
        # self.client.get("maritime/assets/js/jquery.validationEngine-en.js")
        # self.client.get("maritime/assets/js/sweetalert2@9.js")
        # self.client.get("maritime/assets/js/jquery.fancybox.min.js")
        # self.client.get("maritime/aun-responsive.css")
        # self.client.get("maritime/assets/images/loadingimage.gif")
        # self.client.get("assets/images/loadingimage.gif")
        # self.client.get("maritime/assets/images/Lobby_BG.jpg?v=1617181381")
        # self.client.get("maritime/assets/images/lobby_icon.png")
        # self.client.get("maritime/assets/images/exhibition_icon.png")
        # self.client.get("maritime/assets/images/auditorium_icon.png")
        # self.client.get("maritime/assets/images/vip_meeting_room_icon.png")
        #
        # self.client.get("maritime/assets/images/user_right.png")
        # self.client.get("maritime/assets/images/searchh.png")
        #
        # #Fail
        # self.client.get("maritime/assets/font/roboto/Roboto-Bold.woff2")
        # self.client.get("maritime/assets/font/roboto/Roboto-Light.woff2")
        #
        # self.client.get("maritime/assets/images/reception-to-auditorium.mp4")
        # self.client.get("maritime/assets/images/reception-to-exhibition.mp4")
        # self.client.get("maritime/assets/images/reception-to-b2b.mp4")
        # self.client.get("maritime/assets/images/networklounge.mp4")
        #
        # #Fail
        # self.client.get("maritime/assets/font/roboto/Roboto-Bold.woff")
        # self.client.get("maritime/assets/font/roboto/Roboto-Light.woff")
        # self.client.get("maritime/assets/font/roboto/Roboto-Bold.ttf")
        # self.client.get("maritime/assets/font/roboto/Roboto-Light.ttf")
        #
        # self.client.get("maritime/assets/css/bootstrap.min.css")
        #
        #
        #
        # #pavilion
        # self.client.get("maritime/pavilion.php")
        # self.client.get("maritime/assets/images/pavilion-icon.jpg")
        #
        #
        # #Exhibition
        # self.client.get("maritime/hall1.php?id=MQ==")
        # self.client.get("maritime/assets/images/loadingimage.gif")
        # self.client.get("maritime/assets/css/style.css?v=1617183050")
        # self.client.get("maritime/assets/images/beep.gif")
        # self.client.get("maritime/assets/images/hall/HallOptions_Gr1.jpg?v=1617183050")
        #
        # # Auditorium
        # self.client.get("maritime/audi-lobby.php")
        # self.client.get("maritime/assets/css/mdb.min.css")
        # self.client.get("maritime/assets/css/validationEngine.jquery.css")
        # self.client.get("maritime/assets/css/jquery.fancybox.min.css")
        # self.client.get("maritime/assets/css/style.css?v=1617186156")
        # self.client.get("maritime/assets/images/Audi-lobby.jpg?v=1617186156")
        #
        # #networkinglounge
        # self.client.get("maritime/networkinglounge.php")
        # self.client.get("maritime/assets/css/slick-theme.css")
        # self.client.get("maritime/assets/css/style.css?v=1617192199")
        # self.client.get("maritime/assets/images/b2b/background.jpg")
        # self.client.get("maritime/assets/js/slick.min.js")
        #
        # #srchd
        # self.client.get("maritime/srchd.php")


# class WebsiteUser(HttpLocust):
#     task_set = WebsiteTasks
