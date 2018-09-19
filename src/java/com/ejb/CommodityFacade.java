/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ejb;

import com.entity.Commodity;
import java.util.List;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

/**
 *
 * @author agno3
 */
@Stateless
public class CommodityFacade extends AbstractFacade<Commodity> {

    @PersistenceContext(unitName = "AntiqueIDPU")
    private EntityManager em;

    @Override
    protected EntityManager getEntityManager() {
        return em;
    }

    public CommodityFacade() {
        super(Commodity.class);
    }
    public List Search(){
        return em.createNativeQuery("SELECT comm_startprice FROM Commodity c WHERE c.price=:comm_startorice").getResultList();
    }
}
