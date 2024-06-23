###### Problem 2: The Blackjack Game
import random
import time

#### Preprocessing

## 初始化
suits = ["SPADE", "HEART", "DIAMOND", "CLUB"]
ranks = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"]

## 洗牌
decks = []
for i in ranks :
    for j in suits :
        decks.append([str(i),j])

random.shuffle(decks) # 結構 : [花色,點數]


#### Settle the Stage (Game Logic)

trigger = True

#### step1. 最外層while迴圈控制"每一場"遊戲(由y/n控制)
while trigger :

    # 初始化(每場遊戲)
    player_card = []
    dealer_card = []
    player_total = 0
    dealer_total = 0

    # 隨機取出4張牌並隨機分配給玩家和莊家
    for i in range(0,4) :
        if i < 2 :
            player_card.append(decks.pop(i))
        else :
            dealer_card.append(decks.pop(i))
    print(player_card,dealer_card)


    #### step2. 中間while迴圈控制"每回合"(玩家和莊家各完成一回合)

    ## 玩家是否叫牌(Hit)來決定玩家的一回合
    choice = 1  # 初始化(表示叫牌)
    player_i_th_card = 2 # 表示取出玩家第幾張牌

    print("%s %s %s"%("-"*30,"Player Round","-"*30))
    print()

    while choice :    
    
        #### Compute the Total Value of player

        player_total = 0 # 每回合清空玩家分數, 重新計算
        for i in player_card :
            if i[0] in ["2", "3", "4", "5", "6", "7", "8", "9", "10"] :
                score = int(i[0])
                player_total += score
            elif i[0] in ["JACK", "QUEEN", "KING"] :
                score = 10
                player_total += score          
            else :
                check = player_total # 判別加總後分數是否>=21, 來決定ACE的值
                if (check + 11) <= 21 :
                    score = 11
                    player_total += score
                else : 
                    score = 1
                    player_total += score

        #### step3. 玩家回合

        # 印出玩家當前分數和手牌
        if player_total < 21 :
            print("You current value is : %d"%(player_total))
        elif player_total == 21 :
            print("You current value is Blackjack! (21)")
        else :
            print("You current value is Bust! (>21)")

        new_player_card = ["-".join(i) for i in player_card]
        print("with the hand: %s"%(", ".join(new_player_card)))
        print()

        while True :
            choice = input("Hit or stay? (Hit = 1, Stay = 0): ")
            print()
            if choice not in ["0","1"] : # 確認使用者輸入正確的參數
                print("Please enter the valid number! (Hit = 1, Stay = 0)")
                print()
                continue

            else :
                choice = int(choice)
                if choice == 1 : # choose Hit
                    player_card.append(decks.pop(0))
                    print("You draw %s"%("-".join(player_card[player_i_th_card])))
                    player_i_th_card += 1 # 並列印出抽到哪張牌
                
                else : # choose Stay
                    if player_total < 21 :
                        print("You current value is : %d"%(player_total))
                    elif player_total == 21 :
                        print("You current value is Blackjack! (21)")
                    else :
                        print("You current value is Bust! (>21)")
                        choice = 0

                    print("with the hand: %s"%(", ".join(new_player_card)))
                    print()
                    
            break

    print("-"*74)

    #### step4. 莊家回合

    dealer_i_th_card = 2 # 表示取出莊家第幾張牌

    print("%s %s %s"%("-"*30,"Dealer Round","-"*30))
    print()

    #### Compute the Total Value of dealer

    trigger_dealer_hit_or_not = True # 判別莊家的分數是否>17, 來決定是否繼續叫牌

    while trigger_dealer_hit_or_not :
        
        dealer_total = 0 # 每回合清空莊家分數, 重新計算
        for j in dealer_card :
            if j[0] in ["2", "3", "4", "5", "6", "7", "8", "9", "10"] :
                score = int(j[0])
                dealer_total += score
            elif j[0] in ["JACK", "QUEEN", "KING"] :
                score = 10
                dealer_total += score
            
            else :
                check = dealer_total
                if (check + 11) <= 21 :
                    score = 11
                    dealer_total += score
                else : 
                    score = 1
                    dealer_total += score

        # 印出莊家當前分數和手牌
        if dealer_total < 21 :
            print("Dealer's current value is : %d"%(dealer_total))
        elif dealer_total == 21 :
            print("Dealer's current value is Blackjack! (21)")
        else :
            print("Dealer's current value is Bust! (>21)")
        
        new_dealer_card = ["-".join(i) for i in dealer_card]
        print("with the hand: %s"%(", ".join(new_dealer_card)))
        print()

        ## The dealer’s hand is worth less than 17, the dealer is made to hit!
        if dealer_total < 17 :
            dealer_card.append(decks.pop(0))
            print("Dealer draws %s"%("-".join(dealer_card[dealer_i_th_card])))
            print()
            dealer_i_th_card += 1
            
            continue
        else :
            trigger_dealer_hit_or_not = False
    
    print("-"*74)

    #### step5. 判別勝負

    # 玩家勝利 : (玩家拿到21點且莊家沒拿到) or (玩家沒爆牌且莊家爆牌) or (21>=玩家分數>莊家分數) 
    if (player_total == 21 and dealer_total != 21) or (player_total <= 21 and dealer_total > 21) or (21 >= player_total > dealer_total) :
        print("*** You beat the dealer! ***")

    # 莊家勝利 : (玩家爆牌且莊家沒爆牌) or (21>=莊家分數>玩家分數) 
    elif (player_total > 21 >= dealer_total) or (21 >= dealer_total > player_total):
        print("*** Dealer wins! ***" )

    # 平手狀況
    elif player_total == dealer_total :
        print("*** You tied the dealer, nobody wins! ***")

    #### step6. 當分出勝負時, 詢問玩家是否要進行"下一場"遊戲
    while True :
        answer = input("Want to play again? (y/n): ")
        if answer.lower() not in ["y","n"] :
            print("Please enter \'y\' or \'n\' ")
            continue
        if answer.lower() == "n" :  
            trigger = False

        print("-"*74)        
        break

