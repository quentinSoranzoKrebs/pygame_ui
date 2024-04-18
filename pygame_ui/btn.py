
class btn:
    def __init__(self,
                 command = None,
                 text: str = None,
                 image:pygame.surface = None,
                 marge:Union[float,int] = 2,
                 round:Union[float,int] = 4,
                 initial_color:Tuple[int,int,int] = (200,200,200,200),
                 final_color:Tuple[int,int,int] = (0,115,229,255),
                 text_color:Tuple[int,int,int] = BLANC,
                 text_taille:int = 50,
                 width:int = None,
                 height:int = None,
                 line_epaisseur:Union[int,float] = 1
                 ):
        
        if width and height:
            self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

        self.id = id(self)
        print(self.id)
        self.color = initial_color
        self.initial_color = initial_color
        self.final_color = final_color
        self.round = round
        self.clic = False
        self.line_epaisseur = line_epaisseur
        self.line_epaisseur_origin = line_epaisseur
        button = pygame.USEREVENT + 1
        self.event = pygame.event.Event(button, message="Mon événement personnalisé")
        self.anchorx = 0
        self.anchory = 0

        if command:
            self.command = command

        if text:
            self.text = ecrire(text_color,text,text_taille)
            if not width and not height:
                self.surface = pygame.Surface((self.text.get_width()+self.text.get_height(), self.text.get_height()+self.text.get_height()/marge), pygame.SRCALPHA)   
                self.rect = self.surface.get_rect()
            self.surface.blit(self.text,((self.surface.get_width()-self.text.get_width())/2,(self.surface.get_height()-self.text.get_height())/2))
        
        if image:            
            if not width and not height:
                self.surface = pygame.Surface((image.get_width()+image.get_width()/marge, image.get_width()+image.get_width()/marge), pygame.SRCALPHA)   
                self.rect = self.surface.get_rect()
                draw_rounded_rect(self.surface, self.color, self.rect, round)     
            self.surface.blit(image,(0,0))
        self.rect = self.surface.get_rect()
        liste_bouton.append(self)

        self.surface_fond = pygame.Surface((self.surface.get_width(),self.surface.get_height()), pygame.SRCALPHA)

    def update(self,
               event):
        w,h = pygame.display.get_surface().get_size()
        rect = pygame.Rect(self.pos[0]*w-self.anchorx,self.pos[1]*h-self.anchory,self.rect[2],self.rect[3])
        point = pygame.mouse.get_pos()
        collide = rect.collidepoint(point)
        self.color = self.initial_color
        self.line_epaisseur = self.line_epaisseur_origin
        if collide:
            self.color = self.final_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'id': self.id}))
                    self.command()
        
    def draw(self,
             surface):
        w,h = pygame.display.get_surface().get_size()
        rect = pygame.Rect(0,0,self.rect[2],self.rect[3])
        draw_bord(self.surface_fond, self.color, rect, self.surface.get_height()/self.round,self.line_epaisseur+1)
        surface.blit(self.surface_fond,(self.pos[0]*w-self.anchorx,self.pos[1]*h-self.anchory))
        surface.blit(self.surface,(self.pos[0]*w-self.anchorx,self.pos[1]*h-self.anchory))
        
    def place(self,
              x,
              y,
              anchor:str = "nw"):
        if anchor == "nw":
            self.anchorx = 0
            self.anchory = 0
        elif anchor == "n":
            self.anchorx = self.surface.get_width()/2
            self.anchory = 0
        elif anchor == "ne":
            self.anchorx = self.surface.get_width()
            self.anchory = 0
        elif anchor == "center":
            self.anchorx = self.surface.get_width()/2
            self.anchory = self.surface.get_height()/2
        elif anchor == "sw":
            self.anchorx = 0
            self.anchory = self.surface.get_height()
        elif anchor == "s":
            self.anchorx = self.surface.get_width()/2
            self.anchory = self.surface.get_height()
        elif anchor == "se":
            self.anchorx = self.surface.get_width()
            self.anchory = self.surface.get_height()

        self.anchorx
        w,h = pygame.display.get_surface().get_size()
        self.pos = (x,y)
