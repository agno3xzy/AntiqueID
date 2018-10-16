/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ejb;

import com.entity.Expert;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

/**
 *
 * @author agno3
 */
@Stateless
public class ExpertFacade extends AbstractFacade<Expert> {

    @PersistenceContext(unitName = "AntiqueIDPU")
    private EntityManager em;

    @Override
    protected EntityManager getEntityManager() {
        return em;
    }

    public ExpertFacade() {
        super(Expert.class);
    }
    
}
